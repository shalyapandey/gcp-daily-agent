# ☁️ Google Cloud Daily Briefing Agent

An autonomous, serverless AI agent that tracks newly released features, deprecations, and announcements across Google Cloud on a daily basis, synthesizes them using **Google Gemini**, and delivers an executive briefing via **GitHub Actions**, **Slack**, **Discord**, or git-versioned markdown archives.

---

## 🌟 Key Features

* **Real-time Feed Ingestion**: Ingests the official [Google Cloud Release Notes Atom Feed](https://cloud.google.com/feeds/gcp-release-notes.xml) and [Google Cloud Blog RSS](https://cloud.google.com/blog/rss).
* **AI-Powered Synthesis**: Uses `gemini-2.5-flash` via the modern `google-genai` SDK to categorize updates into:
  * ⚡ **Executive Summary**
  * 🚀 **Key Highlights & Major Launches**
  * ⚠️ **Breaking Changes & Deprecations** (EOS warnings, migration deadlines)
  * 🛠️ **Categorized Feature Updates** (AI/ML, Compute, Databases, Security, Networking)
  * 💡 **Architect's Takeaway**
* **Serverless & 100% Free**: Operates entirely within GitHub Actions scheduled cron runs and the free tier of the Gemini API.
* **Multi-Channel Delivery**:
  * **GitHub Actions Job Summary**: Rendered directly in GitHub.
  * **Repository History**: Commits each day's digest to `digests/YYYY-MM-DD.md`.
  * **Slack / Discord**: Dispatches formatted notifications to your team's channels.

---

## 📂 Project Structure

```
gcp-daily-agent/
├── .github/
│   └── workflows/
│       └── daily-briefing.yml   # Scheduled GitHub Actions cron workflow
├── digests/                     # Persistent archive of daily markdown briefings
│   ├── latest.md
│   └── YYYY-MM-DD.md
├── src/
│   ├── __init__.py
│   ├── config.py                # Environment and feed settings
│   ├── fetcher.py               # Atom/RSS ingestion and HTML parsing
│   ├── synthesizer.py           # Gemini prompt engineering & synthesis
│   └── notifier.py              # Webhook and markdown dispatching
├── main.py                      # CLI entrypoint
├── requirements.txt             # Python dependencies
├── .env.example                 # Environment variables template
└── README.md
```

---

## 🚀 Quick Setup (GitHub Actions)

### Step 1: Create a GitHub Repository
1. Initialize a new git repository in this directory:
   ```bash
   git init
   git add .
   git commit -m "feat: initial gcp daily agent setup"
   ```
2. Create a new repository on [GitHub](https://github.com/new).
3. Push your repository:
   ```bash
   git remote add origin https://github.com/<your-username>/<your-repo-name>.git
   git branch -M main
   git push -u origin main
   ```

### Step 2: Configure Repository Secrets
1. Go to your repository on GitHub: **Settings** > **Secrets and variables** > **Actions**.
2. Click **New repository secret** and add:
   * `GEMINI_API_KEY`: *(Required)* Your Google Gemini API key. (Get one for free at [Google AI Studio](https://aistudio.google.com/app/apikey)).
   * `SLACK_WEBHOOK_URL`: *(Optional)* Incoming webhook URL for your Slack channel.
   * `DISCORD_WEBHOOK_URL`: *(Optional)* Incoming webhook URL for your Discord channel.

### Step 3: Enable Workflow Write Permissions
To allow GitHub Actions to commit daily digest files back to your repository:
1. Go to **Settings** > **Actions** > **General**.
2. Under **Workflow permissions**, select **Read and write permissions**.
3. Click **Save**.

### Step 4: Test Run
1. Go to the **Actions** tab in your repository.
2. Under all workflows, click **GCP Daily Briefing Agent**.
3. Click **Run workflow** > **Run workflow**.
4. Check the completed run to view the generated summary under **Job summary** and in the committed `digests/` folder!

---

## 💻 Local Development & Testing

### 1. Set Up Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure Environment
```bash
cp .env.example .env
# Edit .env and paste your GEMINI_API_KEY
```

### 3. Run the Agent
```bash
# Standard run (last 24 hours)
python main.py

# Look back over the weekend (e.g., 72 hours)
python main.py --hours-back 72

# Test without sending webhooks
python main.py --dry-run
```

---

## ⚙️ Customization

* **Change the Schedule**: Edit `.github/workflows/daily-briefing.yml` and modify the cron expression:
  ```yaml
  - cron: "0 8 * * *" # Runs daily at 08:00 UTC
  ```
* **Filter Specific Services**: Customize the prompt in [src/synthesizer.py](src/synthesizer.py) to prioritize services like Vertex AI, BigQuery, or Google Kubernetes Engine.
* **Gemini Model**: Change `GEMINI_MODEL=gemini-2.5-pro` in your `.env` or GitHub Secrets for deeper analysis.
