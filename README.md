# sharepoint-pusher

Utilities to create and publish SharePoint news pages using the Microsoft Graph API.

## Setup

```bash
uv venv .venv
uv pip install -r requirements.txt --python .venv/bin/python
```

Copy `.env.example` to `.env` and fill in your credentials.

## Usage

```bash
uv -m news_poster.cli "My Title" "<p>content</p>"
```

## Makefile

For convenience you can use the provided `Makefile`:

```bash
make setup
make run ARGS="My Title <p>content</p>"
make test
```
