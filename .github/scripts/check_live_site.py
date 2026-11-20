"""Check the two public Merchant Center verification URLs using normal DNS."""

from http.client import HTTPSConnection
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By

ROOT = Path(__file__).resolve().parents[2]
DOMAIN = (ROOT / "CNAME").read_text().strip()
PAGES = [
    ("/", "index.html", "text/html"),
    ("/merchantcenter.txt", "merchantcenter.txt", "text/plain"),
]


def check_https(path, filename, media_type):
    connection = HTTPSConnection(DOMAIN, timeout=20)
    try:
        connection.request("GET", path)
        response = connection.getresponse()
        print(f"GET {path}: {response.status}, {response.getheader('Content-Type')}", flush=True)
        assert response.status == 200, (response.status, response.getheader("Location"))
        assert response.getheader("Location") is None
        assert response.getheader("Refresh") is None
        assert response.headers.get_content_type() == media_type
        assert response.read() == (ROOT / filename).read_bytes(), f"Deployed content differs on {path}"
    finally:
        connection.close()


def check_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--incognito")
    with webdriver.Chrome(options=options) as browser:
        browser.set_page_load_timeout(30)
        for path, filename, _ in PAGES:
            url = f"https://{DOMAIN}{path}"
            browser.get(url)
            print(f"Chrome opened {url} and finished at {browser.current_url}", flush=True)
            assert browser.current_url == url
            if path == "/":
                assert browser.title == "ELMNT Health"
                logo = browser.find_element(By.CSS_SELECTOR, "main img")
                assert logo.get_property("naturalWidth") > 0, "The brand logo did not load"
                links = browser.find_elements(By.CSS_SELECTOR, "main a")
                assert {link.get_attribute("href") for link in links} == {
                    "https://terraelmnt.com/",
                    "https://terraelmnt.com/pages/help",
                }
                assert not browser.find_elements(By.CSS_SELECTOR, 'script, meta[http-equiv="refresh" i]')
            else:
                rendered = browser.find_element(By.TAG_NAME, "body").text
                assert rendered.splitlines() == (ROOT / filename).read_text().splitlines()


if __name__ == "__main__":
    for page in PAGES:
        check_https(*page)
    check_browser()
