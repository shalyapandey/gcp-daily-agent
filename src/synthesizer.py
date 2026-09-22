import datetime
import json
from typing import Optional
from urllib.request import Request, urlopen
from urllib.error import URLError

try:
    from google import genai
except ImportError:
    genai = None

from .fetcher import DailyUpdates


SYSTEM_INSTRUCTION = """
You are a Principal Google Cloud Solutions Architect and Cloud Tech Lead.
Your mission is to analyze Google Cloud updates and release notes from the past 24 hours, synthesizing them into a high-value, crisp, and actionable daily briefing.

Formatting Guidelines:
1. Use clean, professional GitHub-flavored Markdown.
2. Group updates logically by impact and domain.
3. Be direct: highlight *what changed* and *why it matters* to cloud engineers and architects.
4. Maintain clickable Markdown links to official documentation whenever available in the source data.
5. Emphasize deprecations, breaking changes, and End-of-Support (EOS) warnings with bolding or alert callouts.

Structure your response with these exact sections:
# ☁️ Google Cloud Daily Briefing — {date}

## ⚡ Executive Summary
(2-3 high-level sentences capturing the day's theme and key announcements)

## 🚀 Key Highlights & Major Launches
(Bullet points of the most impactful 2-4 items, e.g., GA launches, major model releases, infrastructure milestones, with direct links)

## ⚠️ Breaking Changes & Deprecations (If Any)
(Critical section: Deprecations, End-of-Support dates, API version changes, required migration actions. If none, state "No breaking changes or deprecations reported today.")

## 🛠️ Feature Updates by Domain
(Only include subheadings that have updates)
### AI & Machine Learning (Vertex AI, Gemini, AI Infrastructure)
### Compute, Containers & Serverless (GKE, Cloud Run, GCE)
### Data Analytics & Databases (BigQuery, Spanner, AlloyDB, etc.)
### Security, Identity & Governance (IAM, Secret Manager, Cloud Armor)
### Management, Developer Tools & Others

## 💡 Architect's Takeaway
(1-2 actionable sentences: what should engineering teams test, inspect, or prepare for today?)
"""


def format_raw_updates_text(updates: DailyUpdates) -> str:
    """Format raw updates into structured text for LLM ingestion."""
    lines = []
    lines.append(f"Lookback window: Last {updates.lookback_hours} hours")
    lines.append(f"Period: {updates.start_time_utc.isoformat()} to {updates.end_time_utc.isoformat()}")
    lines.append(f"Total Release Notes Items: {len(updates.release_notes)}")
    lines.append(f"Total Blog Articles: {len(updates.blog_posts)}\n")

    if updates.release_notes:
        lines.append("=== GOOGLE CLOUD RELEASE NOTES ===")
        for item in updates.release_notes:
            link_str = f" [Links: {', '.join(item.links)}]" if item.links else ""
            lines.append(
                f"- Product: {item.product}\n"
                f"  Type: {item.change_type}\n"
                f"  Date: {item.published_date}\n"
                f"  Details: {item.description}{link_str}\n"
            )

    if updates.blog_posts:
        lines.append("\n=== GOOGLE CLOUD BLOG POSTS ===")
        for post in updates.blog_posts:
            lines.append(
                f"- Title: {post.title}\n"
                f"  Date: {post.published_date}\n"
                f"  URL: {post.link}\n"
                f"  Summary: {post.summary}\n"
            )

    return "\n".join(lines)


def generate_fallback_summary(updates: DailyUpdates) -> str:
    """Fallback generator when Gemini API is unavailable or running offline."""
    today = datetime.datetime.now(datetime.timezone.utc).strftime("%B %d, %Y")

    if updates.total_count == 0:
        return f"""# ☁️ Google Cloud Daily Briefing — {today}

## ⚡ Executive Summary
No official release notes or blog updates were recorded for Google Cloud in the past {updates.lookback_hours} hours. All services remain on steady state.

## 🛠️ Status Check
- Checked feeds: Google Cloud Release Notes Atom & GCP Blog.
- Window: {updates.start_time_utc.strftime('%Y-%m-%d %H:%M UTC')} - {updates.end_time_utc.strftime('%Y-%m-%d %H:%M UTC')}.
"""

    lines = [f"# ☁️ Google Cloud Daily Briefing — {today}\n"]
    lines.append("## ⚡ Executive Summary")
    lines.append(f"Found {updates.total_count} updates across Google Cloud in the past {updates.lookback_hours} hours.\n")

    if updates.release_notes:
        lines.append("## 🛠️ Release Notes")
        grouped = {}
        for item in updates.release_notes:
            grouped.setdefault(item.product, []).append(item)

        for product, items in grouped.items():
            lines.append(f"### {product}")
            for item in items:
                links_text = " ".join([f"[Doc]({l})" for l in item.links])
                lines.append(f"- **[{item.change_type}]**: {item.description} {links_text}".strip())
            lines.append("")

    if updates.blog_posts:
        lines.append("## 📰 Google Cloud Blog Posts")
        for post in updates.blog_posts:
            lines.append(f"- [{post.title}]({post.link}): {post.summary}")
        lines.append("")

    return "\n".join(lines)


def call_gemini_rest_api(api_key: str, model_name: str, prompt: str, system_prompt: str) -> Optional[str]:
    """Fallback caller using standard library HTTP request to Google Gemini REST API."""
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={api_key}"
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "systemInstruction": {"parts": [{"text": system_prompt}]},
        "generationConfig": {"temperature": 0.2},
    }
    data = json.dumps(payload).encode("utf-8")
    req = Request(url, data=data, headers={"Content-Type": "application/json"})

    try:
        with urlopen(req, timeout=30) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            return body["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        print(f"[Error] Gemini REST request failed: {e}")
        return None


def synthesize_briefing(
    updates: DailyUpdates,
    api_key: Optional[str] = None,
    model_name: str = "gemini-2.5-flash",
) -> str:
    """Synthesize updates into an executive daily briefing using Gemini."""
    today_str = datetime.datetime.now(datetime.timezone.utc).strftime("%B %d, %Y")
    system_prompt = SYSTEM_INSTRUCTION.format(date=today_str)

    if updates.total_count == 0:
        return f"""# ☁️ Google Cloud Daily Briefing — {today_str}

## ⚡ Executive Summary
No new official Google Cloud release updates or announcements were published in the last {updates.lookback_hours} hours.

- **Status**: All systems steady.
- **Monitoring Window**: {updates.start_time_utc.strftime('%Y-%m-%d %H:%M UTC')} to {updates.end_time_utc.strftime('%Y-%m-%d %H:%M UTC')}.
"""

    raw_text = format_raw_updates_text(updates)

    if not api_key:
        print("[Notice] No GEMINI_API_KEY provided; generating structured markdown fallback.")
        return generate_fallback_summary(updates)

    prompt = f"Date: {today_str}\n\nAnalyze the following raw updates and generate today's briefing:\n\n{raw_text}"

    # Priority 1: Use google-genai official SDK
    if genai is not None:
        try:
            client = genai.Client(api_key=api_key)
            response = client.models.generate_content(
                model=model_name,
                contents=prompt,
                config={
                    "system_instruction": system_prompt,
                    "temperature": 0.2,
                },
            )
            return response.text
        except Exception as e:
            print(f"[Error] google-genai SDK call failed: {e}. Trying REST fallback.")

    # Priority 2: Use direct REST API
    rest_result = call_gemini_rest_api(api_key, model_name, prompt, system_prompt)
    if rest_result:
        return rest_result

    # Priority 3: Fallback summary
    return generate_fallback_summary(updates)
