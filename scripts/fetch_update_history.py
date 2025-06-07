import requests
import os
from datetime import datetime

REPO = "ayapk/rebuilt-site"  # Change to your repo
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
        f.write(f"- **{pr['title']}** ([#{pr['number']}]({pr['html_url']})) — merged at {pr['merged_at'][:10]}\n")

print("Update history written to content/update-history.md")