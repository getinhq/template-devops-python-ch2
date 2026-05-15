import scraper


def test_scrape_titles_baseline():
    assert scraper.scrape_titles("<html></html>") == []
