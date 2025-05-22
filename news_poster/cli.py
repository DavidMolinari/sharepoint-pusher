"""Command line interface for creating SharePoint news."""

from __future__ import annotations

import argparse

from .models import Article
from .sharepoint import create_news, publish_page


def main() -> None:
    parser = argparse.ArgumentParser(description="Publish news to SharePoint")
    parser.add_argument("title", help="Title of the article")
    parser.add_argument("html", help="HTML content of the article")
    args = parser.parse_args()

    article = Article(title=args.title, html=args.html)
    page_id = create_news(article.title, article.html)
    publish_page(page_id)
    print(f"Published page with id {page_id}")


if __name__ == "__main__":
    main()
