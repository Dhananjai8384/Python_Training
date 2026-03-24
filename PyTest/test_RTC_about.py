from playwright.sync_api import sync_playwright

class TestRTCAbout:

    def about_page_status(self, page):

        base_url = "https://rtctek.com"

        # Open website
        page.goto(base_url)

        # Set browser size (Playwright alternative to maximize)
        page.set_viewport_size({"width": 1920, "height": 1080})

        # Click on About Us
        page.click("text=About Us")

        # Wait for page to load
        page.wait_for_load_state("load")

        # Get current URL
        current_url = page.url
        print(f"Current URL: {current_url}")

        # Expected URL
        expected_url = base_url + "/about-us/"

        print(f"Expected URL: {expected_url}")

        # Assertion
        assert current_url == expected_url, f"URL mismatch: {current_url} != {expected_url}"


def test_RTC_about():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        obj = TestRTCAbout()
        obj.about_page_status(page)

        browser.close()