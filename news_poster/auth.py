"""Authentication helper using MSAL."""

from __future__ import annotations

import os
from typing import Optional

from msal import ConfidentialClientApplication

from .config import get_config


def get_token(scope: str = "https://graph.microsoft.com/.default") -> str:
    """Acquire an access token for Microsoft Graph."""
    cfg = get_config()
    app = ConfidentialClientApplication(
        client_id=cfg.CLIENT_ID,
        authority=f"https://login.microsoftonline.com/{cfg.TENANT_ID}",
        client_credential=cfg.CLIENT_SECRET,
    )
    result: Optional[dict] = app.acquire_token_for_client(scopes=[scope])
    if not result or "access_token" not in result:
        raise RuntimeError("Failed to obtain access token")
    return str(result["access_token"])
