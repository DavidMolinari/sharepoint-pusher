"""Wrapper around Microsoft Graph API for SharePoint news."""

from __future__ import annotations

import os
from typing import Dict, Any

import requests

from .auth import get_token
from .config import get_config

GRAPH_ROOT = "https://graph.microsoft.com/v1.0"


def _headers() -> Dict[str, str]:
    token = get_token()
    return {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}


def create_news(title: str, html: str) -> str:
    """Create a news page and return its page ID."""
    cfg = get_config()
    payload = {
        "title": title,
        "pageLayout": "Article",
        "promotionKind": "newsPost",
        "webParts": [{"type": "rte", "innerHtml": html}],
    }
    resp = requests.post(
        f"{GRAPH_ROOT}/sites/{cfg.SITE_ID}/pages", headers=_headers(), json=payload
    )
    resp.raise_for_status()
    data = resp.json()
    return data["id"]


def publish_page(page_id: str) -> None:
    cfg = get_config()
    url = f"{GRAPH_ROOT}/sites/{cfg.SITE_ID}/pages/{page_id}/microsoft.graph.sitePage/publish"
    resp = requests.post(url, headers=_headers())
    resp.raise_for_status()
