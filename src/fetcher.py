import datetime
import re
from dataclasses import dataclass, field
from typing import List, Optional
import xml.etree.ElementTree as ET
from html.parser import HTMLParser

try:
    import feedparser
except ImportError:
    feedparser = None

try:
    from bs4 import BeautifulSoup
except ImportError:
    BeautifulSoup = None

try:
    import requests
except ImportError:
    requests = None

try:
    from dateutil import parser as date_parser
except ImportError:
    date_parser = None

from urllib.request import urlopen, Request


@dataclass
class ReleaseNoteItem:
    """Individual product release note entry."""
    product: str
    change_type: str
    description: str
    links: List[str] = field(default_factory=list)
    published_date: Optional[str] = None


@dataclass
class BlogItem:
    """Google Cloud blog announcement."""
    title: str
    link: str
    summary: str
    published_date: Optional[str] = None


@dataclass
class CommunityItem:
    """Community article or ecosystem update (e.g. from SnowNews, Medium)."""
    title: str
    link: str
    source: str  # e.g. Medium, Google Workspace Updates, Cloud Blog
    published_date: Optional[str] = None


@dataclass
class DailyUpdates:
    """Aggregated updates for the lookback period."""
    lookback_hours: int
    start_time_utc: datetime.datetime
    end_time_utc: datetime.datetime
    release_notes: List[ReleaseNoteItem] = field(default_factory=list)
    blog_posts: List[BlogItem] = field(default_factory=list)
    community_articles: List[CommunityItem] = field(default_factory=list)

    @property
    def total_count(self) -> int:
        return len(self.release_notes) + len(self.blog_posts) + len(self.community_articles)


class SimpleHTMLTextExtractor(HTMLParser):
    """Fallback HTML parser using standard library when BeautifulSoup is not installed."""
    def __init__(self):
        super().__init__()
        self.text_parts = []
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for k, v in attrs:
                if k == "href":
                    href = v.strip()
                    if href.startswith("/"):
                        href = f"https://cloud.google.com{href}"
                    self.links.append(href)

    def handle_data(self, data):
        cleaned = data.strip()
        if cleaned:
            self.text_parts.append(cleaned)

    def get_text(self):
        return " ".join(self.text_parts)


def parse_date_string(date_str: str) -> Optional[datetime.datetime]:
    """Parse an ISO or RFC date string into timezone-aware UTC datetime."""
    if date_parser is not None:
        try:
            dt = date_parser.parse(date_str)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=datetime.timezone.utc)
            return dt.astimezone(datetime.timezone.utc)
        except Exception:
            pass

    # Standard library email.utils for RFC 2822 / RSS pubDate (e.g., 'Tue, 22 Sep 2026 19:41:32 +0000')
    try:
        import email.utils
        dt = email.utils.parsedate_to_datetime(date_str)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=datetime.timezone.utc)
        return dt.astimezone(datetime.timezone.utc)
    except Exception:
        pass

    # Built-in fromisoformat (Python 3.11+)
    try:
        dt = datetime.datetime.fromisoformat(date_str)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=datetime.timezone.utc)
        return dt.astimezone(datetime.timezone.utc)
    except Exception:
        pass

    # Basic fallback regex for YYYY-MM-DD
    match = re.match(r"^(\d{4})-(\d{2})-(\d{2})", date_str)
    if match:
        year, month, day = map(int, match.groups())
        return datetime.datetime(year, month, day, tzinfo=datetime.timezone.utc)
    return None


def parse_release_notes_html(html_content: str, date_str: str) -> List[ReleaseNoteItem]:
    """Extract release note items from HTML body."""
    if BeautifulSoup:
        soup = BeautifulSoup(html_content, "html.parser")
        items: List[ReleaseNoteItem] = []
        current_product = "General / Multi-Product"
        current_type = "Update"
        current_desc_parts: List[str] = []
        current_links: List[str] = []

        def flush():
            nonlocal current_desc_parts, current_links
            text = " ".join(current_desc_parts).strip()
            if text:
                items.append(
                    ReleaseNoteItem(
                        product=current_product,
                        change_type=current_type,
                        description=text,
                        links=list(dict.fromkeys(current_links)),
                        published_date=date_str,
                    )
                )
            current_desc_parts = []
            current_links = []

        for tag in soup.find_all(["h2", "h3", "p", "ul", "ol"]):
            if tag.name == "h2":
                flush()
                current_product = tag.get_text(strip=True)
                current_type = "Update"
            elif tag.name == "h3":
                flush()
                current_type = tag.get_text(strip=True)
            elif tag.name in ("p", "ul", "ol"):
                for a in tag.find_all("a", href=True):
                    href = a["href"].strip()
                    if href.startswith("/"):
                        href = f"https://cloud.google.com{href}"
                    current_links.append(href)
                text = tag.get_text(separator=" ", strip=True)
                if text:
                    current_desc_parts.append(text)
        flush()
        return items
    else:
        # Standard library fallback parser using regex chunks
        items: List[ReleaseNoteItem] = []
        sections = re.split(r"<h2[^>]*>(.*?)</h2>", html_content, flags=re.DOTALL)
        if len(sections) > 1:
            for i in range(1, len(sections), 2):
                product_name = re.sub(r"<[^>]+>", "", sections[i]).strip()
                body = sections[i + 1] if i + 1 < len(sections) else ""
                
                # Split by h3
                subsections = re.split(r"<h3[^>]*>(.*?)</h3>", body, flags=re.DOTALL)
                if len(subsections) > 1:
                    for j in range(1, len(subsections), 2):
                        change_type = re.sub(r"<[^>]+>", "", subsections[j]).strip()
                        sub_body = subsections[j + 1] if j + 1 < len(subsections) else ""
                        parser = SimpleHTMLTextExtractor()
                        parser.feed(sub_body)
                        desc = parser.get_text()
                        if desc:
                            items.append(
                                ReleaseNoteItem(
                                    product=product_name,
                                    change_type=change_type,
                                    description=desc,
                                    links=list(dict.fromkeys(parser.links)),
                                    published_date=date_str,
                                )
                            )
                else:
                    parser = SimpleHTMLTextExtractor()
                    parser.feed(body)
                    desc = parser.get_text()
                    if desc:
                        items.append(
                            ReleaseNoteItem(
                                product=product_name,
                                change_type="Update",
                                description=desc,
                                links=list(dict.fromkeys(parser.links)),
                                published_date=date_str,
                            )
                        )
        return items


def fetch_raw_feed_text(source: str) -> str:
    """Fetch text from URL or read local file path."""
    if source.startswith("http://") or source.startswith("https://"):
        if requests:
            headers = {"User-Agent": "GCP-Daily-Briefing-Agent/1.0"}
            resp = requests.get(source, headers=headers, timeout=20)
            resp.raise_for_status()
            return resp.text
        else:
            req = Request(source, headers={"User-Agent": "GCP-Daily-Briefing-Agent/1.0"})
            with urlopen(req, timeout=20) as resp:
                return resp.read().decode("utf-8")
    else:
        with open(source, "r", encoding="utf-8") as f:
            return f.read()


def fetch_updates(
    release_notes_source: str,
    blog_source: Optional[str] = None,
    snownews_source: Optional[str] = None,
    lookback_hours: int = 24,
    include_blog: bool = True,
    include_snownews: bool = True,
) -> DailyUpdates:
    """Fetch and aggregate updates within the lookback window."""
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    cutoff_utc = now_utc - datetime.timedelta(hours=lookback_hours)

    updates = DailyUpdates(
        lookback_hours=lookback_hours,
        start_time_utc=cutoff_utc,
        end_time_utc=now_utc,
    )

    seen_links = set()

    # 1. Fetch GCP Release Notes (Atom)
    try:
        raw_xml = fetch_raw_feed_text(release_notes_source)
        if feedparser:
            feed = feedparser.parse(raw_xml)
            for entry in feed.entries:
                updated_str = getattr(entry, "updated", getattr(entry, "published", None))
                entry_dt = parse_date_string(updated_str) if updated_str else None
                if entry_dt and entry_dt >= cutoff_utc:
                    html_body = ""
                    if hasattr(entry, "content") and entry.content:
                        html_body = entry.content[0].value
                    elif hasattr(entry, "summary"):
                        html_body = entry.summary
                    items = parse_release_notes_html(html_body, entry_dt.strftime("%Y-%m-%d"))
                    updates.release_notes.extend(items)
        else:
            clean_xml = re.sub(r'xmlns="[^"]+"', '', raw_xml, count=1)
            root = ET.fromstring(clean_xml)
            for entry in root.findall("entry"):
                updated_elem = entry.find("updated")
                if updated_elem is not None and updated_elem.text:
                    entry_dt = parse_date_string(updated_elem.text)
                    if entry_dt and entry_dt >= cutoff_utc:
                        content_elem = entry.find("content")
                        html_body = content_elem.text if content_elem is not None and content_elem.text else ""
                        items = parse_release_notes_html(html_body, entry_dt.strftime("%Y-%m-%d"))
                        updates.release_notes.extend(items)
    except Exception as e:
        print(f"[Warning] Failed to fetch release notes from {release_notes_source}: {e}")

    # 2. Fetch Blog posts
    if include_blog and blog_source:
        try:
            raw_blog = fetch_raw_feed_text(blog_source)
            if feedparser:
                feed = feedparser.parse(raw_blog)
                for entry in feed.entries:
                    dt_str = getattr(entry, "published", getattr(entry, "updated", None))
                    entry_dt = parse_date_string(dt_str) if dt_str else None
                    if entry_dt and entry_dt >= cutoff_utc:
                        link = getattr(entry, "link", "")
                        summary = getattr(entry, "summary", "")
                        summary_clean = re.sub(r"<[^>]+>", "", summary).strip()
                        if link:
                            seen_links.add(link)
                        updates.blog_posts.append(
                            BlogItem(
                                title=getattr(entry, "title", "Untitled"),
                                link=link,
                                summary=summary_clean,
                                published_date=entry_dt.strftime("%Y-%m-%d"),
                            )
                        )
            else:
                clean_xml = re.sub(r'xmlns="[^"]+"', '', raw_blog, count=1)
                root = ET.fromstring(clean_xml)
                for item in root.findall(".//item"):
                    pub_date = item.find("pubDate")
                    entry_dt = parse_date_string(pub_date.text) if pub_date is not None and pub_date.text else None
                    if entry_dt and entry_dt >= cutoff_utc:
                        title_el = item.find("title")
                        link_el = item.find("link")
                        desc_el = item.find("description")
                        link = link_el.text if link_el is not None else ""
                        if link:
                            seen_links.add(link)
                        updates.blog_posts.append(
                            BlogItem(
                                title=title_el.text if title_el is not None else "Untitled",
                                link=link,
                                summary=re.sub(r"<[^>]+>", "", desc_el.text).strip() if desc_el is not None and desc_el.text else "",
                                published_date=entry_dt.strftime("%Y-%m-%d"),
                            )
                        )
        except Exception as e:
            print(f"[Warning] Failed to fetch blog feed from {blog_source}: {e}")

    # 3. Fetch SnowNews feed (Medium community articles & Workspace updates)
    if include_snownews and snownews_source:
        try:
            raw_sn = fetch_raw_feed_text(snownews_source)
            if feedparser:
                feed = feedparser.parse(raw_sn)
                for entry in feed.entries:
                    dt_str = getattr(entry, "published", getattr(entry, "updated", None))
                    entry_dt = parse_date_string(dt_str) if dt_str else None
                    if entry_dt and entry_dt >= cutoff_utc:
                        source_tag = getattr(entry, "description", "Community").strip()
                        # Avoid duplicating release notes which are already parsed from official atom feed
                        if "/release-notes" in link or (source_tag.startswith("(") and source_tag.endswith(")")):
                            continue
                        if link in seen_links:
                            continue
                        seen_links.add(link)
                        updates.community_articles.append(
                            CommunityItem(
                                title=getattr(entry, "title", "Untitled"),
                                link=link,
                                source=source_tag,
                                published_date=entry_dt.strftime("%Y-%m-%d"),
                            )
                        )
            else:
                clean_xml = re.sub(r'xmlns="[^"]+"', '', raw_sn, count=1)
                root = ET.fromstring(clean_xml)
                for item in root.findall(".//item"):
                    pub_date = item.find("pubDate")
                    entry_dt = parse_date_string(pub_date.text) if pub_date is not None and pub_date.text else None
                    if entry_dt and entry_dt >= cutoff_utc:
                        title_el = item.find("title")
                        link_el = item.find("link")
                        desc_el = item.find("description")
                        link = link_el.text.strip() if link_el is not None and link_el.text else ""
                        source_tag = desc_el.text.strip() if desc_el is not None and desc_el.text else "Community"
                        # Avoid duplicating release notes which are already parsed from official atom feed
                        if "/release-notes" in link or (source_tag.startswith("(") and source_tag.endswith(")")):
                            continue
                        if link in seen_links:
                            continue
                        seen_links.add(link)
                        updates.community_articles.append(
                            CommunityItem(
                                title=title_el.text if title_el is not None else "Untitled",
                                link=link,
                                source=source_tag,
                                published_date=entry_dt.strftime("%Y-%m-%d"),
                            )
                        )
        except Exception as e:
            print(f"[Warning] Failed to fetch SnowNews feed from {snownews_source}: {e}")

    return updates
