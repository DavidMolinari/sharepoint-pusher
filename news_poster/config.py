"""Configuration loading using environment variables."""

from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Config:
    TENANT_ID: str
    CLIENT_ID: str
    CLIENT_SECRET: str
    SITE_ID: str


def get_config() -> Config:
    return Config(
        TENANT_ID=os.environ.get("TENANT_ID", ""),
        CLIENT_ID=os.environ.get("CLIENT_ID", ""),
        CLIENT_SECRET=os.environ.get("CLIENT_SECRET", ""),
        SITE_ID=os.environ.get("SITE_ID", ""),
    )
