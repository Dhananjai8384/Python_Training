from playwright.sync_api import sync_playwright

class TestRTCBlogs:

    def blogs_page_status(self, page):

        base_url = "https://rtctek.com"

        # Open website
        page.goto(base_url)

        # Set browser size (equivalent to maximize)
        page.set_viewport_size({"width": 1920, "height": 1080})

        # Click on Knowledge Center
        page.click("text=Knowledge Center")

        # Wait for navigation
        page.wait_for_load_state("load")

        # Get current URL
        current_url = page.url
        print(f"Current URL: {current_url}")

        # Expected URL
        expected_url = base_url + "/blogs/"

        print(f"Expected URL: {expected_url}")

        # Assertion
        assert current_url == expected_url, f"URL mismatch: {current_url} != {expected_url}"


def test_RTC_blogs():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # opens browser
        page = browser.new_page()

        obj = TestRTCBlogs()
        obj.blogs_page_status(page)

        browser.close()