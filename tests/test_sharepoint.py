from __future__ import annotations

import os

import responses
from news_poster.sharepoint import create_news, publish_page, GRAPH_ROOT
from news_poster import config


@responses.activate
def test_create_and_publish(monkeypatch):
    cfg = config.Config(
        TENANT_ID="tenant",
        CLIENT_ID="client",
        CLIENT_SECRET="secret",
        SITE_ID="site",
    )
    monkeypatch.setattr(config, "get_config", lambda: cfg)
    monkeypatch.setattr("news_poster.auth.get_token", lambda scope="": "token")

    responses.post(
        f"{GRAPH_ROOT}/sites/{cfg.SITE_ID}/pages",
        json={"id": "123"},
        status=201,
    )
    responses.post(
        f"{GRAPH_ROOT}/sites/{cfg.SITE_ID}/pages/123/microsoft.graph.sitePage/publish",
        status=200,
    )

    page_id = create_news("title", "<p>body</p>")
    assert page_id == "123"
    publish_page(page_id)
