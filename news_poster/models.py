"""Data models for SharePoint news."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Article:
    """Representation of a SharePoint news article."""

    title: str
    html: str
    banner_image_url: str | None = None
