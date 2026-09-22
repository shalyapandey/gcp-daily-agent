import os
from dataclasses import dataclass
from typing import Optional

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


@dataclass
class Config:
    """Agent runtime configuration settings."""
    gemini_api_key: Optional[str] = os.environ.get("GEMINI_API_KEY")
    gemini_model: str = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")
    
    # Feed Sources
    release_notes_url: str = "https://cloud.google.com/feeds/gcp-release-notes.xml"
    blog_rss_url: str = "https://cloud.google.com/blog/rss"
    
    # Notification targets
    slack_webhook_url: Optional[str] = os.environ.get("SLACK_WEBHOOK_URL")
    discord_webhook_url: Optional[str] = os.environ.get("DISCORD_WEBHOOK_URL")
    github_step_summary_path: Optional[str] = os.environ.get("GITHUB_STEP_SUMMARY")
    
    # Defaults
    lookback_hours: int = int(os.environ.get("LOOKBACK_HOURS", "24"))
    include_blog: bool = os.environ.get("INCLUDE_BLOG", "true").lower() in ("true", "1", "yes")
    digest_dir: str = os.environ.get("DIGEST_DIR", "digests")


config = Config()
