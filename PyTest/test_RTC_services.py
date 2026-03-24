from playwright.sync_api import sync_playwright

class TestRTCServices:

    def services_page_status(self, page):

        base_url = "https://rtctek.com"

        # Open website
        page.goto(base_url)

        # Maximize (Playwright uses viewport instead)
        page.set_viewport_size({"width": 1920, "height": 1080})

        # Click on Services
        page.click("text=Services")

        # Get current URL
        current_url = page.url
        print(f"Current URL: {current_url}")

        # Expected URL
        expected_url = base_url + "/services/"

        print(f"Expected URL: {expected_url}")

        # Assertion
        assert current_url == expected_url, f"URL mismatch: {current_url} != {expected_url}"


def test_RTC_services():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # opens browser
        page = browser.new_page()

        obj = TestRTCServices()
        obj.services_page_status(page)

    