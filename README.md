# Pelican Static Site

This is a static website built with [Pelican](https://getpelican.com/) and Python, managed with [Poetry](https://python-poetry.org/). It features hot-reloading for local development, automated update history from GitHub PRs, and is deployable to Firebase Hosting.

## Features
- **Static site generation** with Pelican
- **Modern, monospaced design** (Open Sauce Mono)
- **Hot reloading** for content and theme changes using Watchdog
- **Automated update history** page from latest merged GitHub PRs
- **Firebase Hosting** deployment

## Getting Started

### Prerequisites
- Python 3.8+
- [Poetry](https://python-poetry.org/docs/#installation)
- [Node.js & npm](https://nodejs.org/) (for Firebase CLI, if deploying)

### Install dependencies
```sh
poetry install
```

### Local Development (with Hot Reload)
This will:
- Fetch the latest update history from GitHub
- Start a local Pelican server
- Watch for changes in `content/` and `theme/` to auto-rebuild

```sh
poetry run python autoreload.py
```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

### Building the Site
To generate the static site in the `output/` directory:
```sh
poetry run pelican content
```

### Deploying to Firebase Hosting
1. Install the Firebase CLI:
   ```sh
   npm install -g firebase-tools
   ```
2. Build the site:
   ```sh
   poetry run pelican content
   ```
3. Deploy:
   ```sh
   firebase deploy
   ```

Optionally this site will autodeploy when merging to the Github `Main` branch.

## Update History Page
The `content/update-history.md` page is automatically generated from the latest merged PRs on GitHub. To update it manually:
```sh
poetry run python scripts/fetch_update_history.py
```

## Configuration
- Edit `pelicanconf.py` to change site settings, navigation, and social links.
- Edit `theme/static/css/style.css` for custom styles.

