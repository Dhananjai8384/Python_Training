from selenium import webdriver
driver = webdriver.Chrome()

class TestRTCAbout:

    def about_page_status(self):

        base_url = "https://rtctek.com"

        driver.get(base_url)
        driver.maximize_window()

        # Click on About Us
        driver.find_element("xpath", "//a[text()='About Us']").click()

        # Get current URL after click
        current_url = driver.current_url
        print(f"Current URL: {current_url}")

        # Expected URL
        expected_url = base_url + "/about-us/"

        print(f"Expected URL: {expected_url}")

        # Assertion
        assert current_url == expected_url, f"URL mismatch: {current_url} != {expected_url}"

def test_RTC_about():
    obj = TestRTCAbout()
    obj.about_page_status()