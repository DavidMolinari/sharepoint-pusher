# sharepoint-pusher

Utilities to create and publish SharePoint news pages using the Microsoft Graph API.

## Setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and fill in your credentials.

## Usage

```bash
python -m news_poster.cli "My Title" "<p>content</p>"
```
