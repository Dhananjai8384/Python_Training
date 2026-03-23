from selenium import webdriver
driver = webdriver.Chrome()

class TestRTCServices:

    def services_page_status(self):

        base_url = "https://rtctek.com"

        driver.get(base_url)
        driver.maximize_window()

        # Click on Services
        driver.find_element("xpath", "//a[text()='Services']").click()

        # Get current URL after click
        current_url = driver.current_url
        print(f"Current URL: {current_url}")

        # Expected URL
        expected_url = base_url + "/services/"

        print(f"Expected URL: {expected_url}")

        # Assertion
        assert current_url == expected_url, f"URL mismatch: {current_url} != {expected_url}"



def test_RTC_services():
    obj = TestRTCServices()
    obj.services_page_status()