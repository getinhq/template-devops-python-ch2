from pathlib import Path

import scraper

FIXTURE = Path(__file__).parent / "fixtures" / "blog.html"


def test_scrape_titles_from_fixture():
    html = FIXTURE.read_text(encoding="utf-8")
    titles = scraper.scrape_titles(html)
    assert titles == ["First Post", "Second Post"]
