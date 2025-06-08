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
        f.write(f"<span class='update-history-pr-title'>**{pr['title']}** ([#{pr['number']}]({pr['html_url']}))</span>\n")
        f.write(f"<span class='update-history-pr-meta'>Merged at {pr['merged_at'][:10]}</span>\n")
        if pr.get('body'):
            body = pr['body'].replace('\r\n', '\n').replace('\r', '\n')
            body = html.escape(body)
            body = body.replace('\n', '<br>')
            f.write(f"<span class='pr-body'>{body}</span>\n")
        f.write("<hr>\n\n")

print("Update history written to content/update-history.md")