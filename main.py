#!/usr/bin/env python3
"""Google Cloud Daily Briefing Agent Entry Point."""

import argparse
import sys
from pathlib import Path
from src.config import config
from src.fetcher import fetch_updates
from src.synthesizer import synthesize_briefing
from src.notifier import (
    save_digest_archive,
    write_github_step_summary,
    send_slack_notification,
    send_discord_notification,
)


def main():
    parser = argparse.ArgumentParser(
        description="Google Cloud Daily Briefing Agent: Track, synthesize, and report GCP updates."
    )
    parser.add_argument(
        "--hours-back",
        type=int,
        default=config.lookback_hours,
        help=f"Number of hours to look back for updates (default: {config.lookback_hours})",
    )
    parser.add_argument(
        "--feed-url",
        type=str,
        default=config.release_notes_url,
        help="URL or local path to GCP release notes Atom feed",
    )
    parser.add_argument(
        "--blog-url",
        type=str,
        default=config.blog_rss_url,
        help="URL or local path to GCP blog RSS feed",
    )
    parser.add_argument(
        "--snownews-url",
        type=str,
        default=config.snownews_feed_url,
        help="URL or local path to SnowNews RSS feed",
    )
    parser.add_argument(
        "--no-blog",
        action="store_true",
        help="Disable fetching Google Cloud Blog posts",
    )
    parser.add_argument(
        "--no-snownews",
        action="store_true",
        help="Disable fetching SnowNews community feed",
    )
    parser.add_argument(
        "--mock-feed",
        type=str,
        help="Path to a local XML file to use instead of fetching live release notes feed",
    )
    parser.add_argument(
        "--mock-snownews-feed",
        type=str,
        help="Path to a local XML file to use instead of fetching live SnowNews feed",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Run without dispatching external webhooks (Slack/Discord)",
    )
    parser.add_argument(
        "--output",
        type=str,
        help="Custom output file path to write markdown summary",
    )

    args = parser.parse_args()

    print("==================================================")
    print(" ☁️  Google Cloud Daily Briefing Agent")
    print("==================================================")
    print(f"Lookback Window: Last {args.hours_back} hours")
    print(f"Gemini Model:    {config.gemini_model}")
    print(f"Dry Run Mode:    {args.dry_run}")

    # Determine feed sources
    feed_source = args.mock_feed if args.mock_feed else args.feed_url
    blog_source = None if (args.no_blog or not config.include_blog or args.mock_feed) else args.blog_url
    snownews_source = args.mock_snownews_feed if args.mock_snownews_feed else (
        None if (args.no_snownews or not config.include_snownews) else args.snownews_url
    )

    print(f"Fetching updates from: {feed_source}")
    updates = fetch_updates(
        release_notes_source=feed_source,
        blog_source=blog_source,
        snownews_source=snownews_source,
        lookback_hours=args.hours_back,
        include_blog=(not args.no_blog and config.include_blog and not args.mock_feed),
        include_snownews=(not args.no_snownews and config.include_snownews),
    )

    print(
        f"[Stats] Fetched {len(updates.release_notes)} release notes, "
        f"{len(updates.blog_posts)} blog posts, "
        f"{len(updates.community_articles)} community articles."
    )

    # Synthesize with Gemini
    print("Synthesizing briefing...")
    briefing_md = synthesize_briefing(
        updates=updates,
        api_key=config.gemini_api_key,
        model_name=config.gemini_model,
    )

    # Save to archive
    archive_path = save_digest_archive(briefing_md, digest_dir=config.digest_dir)

    # Optional custom output
    if args.output:
        out_p = Path(args.output)
        out_p.parent.mkdir(parents=True, exist_ok=True)
        out_p.write_text(briefing_md, encoding="utf-8")
        print(f"Custom output saved to: {out_p}")

    # Publish to GitHub Step Summary (if running in GitHub Actions)
    write_github_step_summary(briefing_md, summary_file=config.github_step_summary_path)

    # Send webhooks if not in dry-run
    if not args.dry_run:
        if config.slack_webhook_url:
            send_slack_notification(config.slack_webhook_url, briefing_md)
        if config.discord_webhook_url:
            send_discord_notification(config.discord_webhook_url, briefing_md)
    else:
        print("[Dry Run] Skipped sending external webhooks.")

    print("==================================================")
    print(" Briefing completed successfully!")
    print(f" Archive: {archive_path}")
    print("==================================================")


if __name__ == "__main__":
    main()
