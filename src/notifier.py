import os
import json
import datetime
from pathlib import Path
from typing import Optional
from urllib.request import Request, urlopen

try:
    import requests
except ImportError:
    requests = None


def post_webhook_json(url: str, payload: dict) -> bool:
    """Send JSON payload to webhook via requests or standard library urllib."""
    if requests is not None:
        try:
            resp = requests.post(url, json=payload, timeout=10)
            return resp.status_code in (200, 204)
        except Exception as e:
            print(f"[Notifier] requests POST failed: {e}")
            return False
    else:
        try:
            data = json.dumps(payload).encode("utf-8")
            req = Request(url, data=data, headers={"Content-Type": "application/json", "User-Agent": "GCP-Agent/1.0"})
            with urlopen(req, timeout=10) as resp:
                return resp.status in (200, 204)
        except Exception as e:
            print(f"[Notifier] urllib POST failed: {e}")
            return False


def save_digest_archive(markdown_content: str, digest_dir: str = "digests") -> Path:
    """Save the briefing markdown into an archived file by date."""
    target_dir = Path(digest_dir)
    target_dir.mkdir(parents=True, exist_ok=True)

    date_str = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
    archive_file = target_dir / f"{date_str}.md"
    archive_file.write_text(markdown_content, encoding="utf-8")

    # Also write a latest.md pointer for easy linking
    latest_file = target_dir / "latest.md"
    latest_file.write_text(markdown_content, encoding="utf-8")

    print(f"[Notifier] Saved digest archive to: {archive_file}")
    return archive_file


def write_github_step_summary(markdown_content: str, summary_file: Optional[str] = None):
    """Write markdown content to GitHub Actions step summary if available."""
    path = summary_file or os.environ.get("GITHUB_STEP_SUMMARY")
    if not path:
        return

    try:
        with open(path, "a", encoding="utf-8") as f:
            f.write(markdown_content + "\n\n")
        print(f"[Notifier] Appended briefing to GitHub Step Summary: {path}")
    except Exception as e:
        print(f"[Warning] Failed to write to GITHUB_STEP_SUMMARY: {e}")


def send_slack_notification(webhook_url: str, markdown_content: str) -> bool:
    """Send summary to Slack via Incoming Webhook."""
    if not webhook_url:
        return False

    preview = markdown_content
    if len(preview) > 3500:
        preview = preview[:3500] + "\n\n*(Truncated. View full digest in repository)*"

    payload = {
        "text": preview,
        "mrkdwn": True,
    }

    ok = post_webhook_json(webhook_url, payload)
    if ok:
        print("[Notifier] Successfully dispatched Slack notification.")
    else:
        print("[Notifier] Failed to send Slack notification.")
    return ok


def send_discord_notification(webhook_url: str, markdown_content: str) -> bool:
    """Send summary to Discord via Webhook (handling 2000 character limit)."""
    if not webhook_url:
        return False

    MAX_DISCORD_LEN = 1900
    chunks = []
    lines = markdown_content.splitlines(keepends=True)
    current_chunk = ""

    for line in lines:
        if len(current_chunk) + len(line) > MAX_DISCORD_LEN:
            chunks.append(current_chunk)
            current_chunk = line
        else:
            current_chunk += line
    if current_chunk:
        chunks.append(current_chunk)

    success = True
    for idx, chunk in enumerate(chunks[:5]):
        if not post_webhook_json(webhook_url, {"content": chunk}):
            print(f"[Notifier] Discord webhook error chunk {idx}")
            success = False

    if success:
        print("[Notifier] Successfully dispatched Discord notification.")
    return success
