import requests
import os
from datetime import datetime
import html

REPO = "AyaPK/rebuilt-site"  # Change to your repo
TOKEN = os.environ.get("GITHUB_TOKEN")  # Set this in your workflow secrets for higher rate limits

headers = {"Accept": "application/vnd.github+json"}
if TOKEN:
    headers["Authorization"] = f"token {TOKEN}"

url = f"https://api.github.com/repos/{REPO}/pulls"
params = {"state": "closed", "per_page": 10, "sort": "updated", "direction": "desc"}

response = requests.get(url, headers=headers, params=params)
response.raise_for_status()

prs = [pr for pr in response.json() if pr["merged_at"]]

with open("content/update-history.md", "w", encoding="utf-8") as f:
    f.write(f"Title: Update History\nDate: {datetime.now().strftime('%Y-%m-%d')}\n\n")
    f.write("# Update History\n\n")
    for pr in prs:
        f.write(f"- **{pr['title']}** ([#{pr['number']}]({pr['html_url']})) — merged at {pr['merged_at'][:10]}\n\n")
        if pr.get("body"):
            body = html.escape(pr["body"]).replace('\n', '<br>')
            f.write(f"<div class='pr-body' style='font-size:0.95em;opacity:0.7;margin-left:1.5em;margin-bottom:1.5em;'>{body}</div>\n")

print("Update history written to content/update-history.md")