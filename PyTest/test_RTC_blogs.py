# import requests
# import webbrowser
# from selenium import webdriver
# driver = webdriver.Chrome()  # Ensure you have the appropriate WebDriver installed and in your PATH

# class TestRTCBlogs:

#     def blogs_page_status(self):

#         driver.get("https://rtctek.com/")
#         driver.maximize_window()
#         driver.find_element("xpath", "//a[text()='Knowledge Center']").click()
#         url = driver.current_url
#         print(f"Current URL: {url}")
#         url = "https://rtctek.com/blogs/"

#         # response = requests.get(url, headers=headers)
#         # print(f"URL: {response.url}")

#         # #assert response.status_code == 200
#         # assert response.url == "https://rtctek.com/blogs/"
#         # webbrowser.open(response.url)

# def test_RTC_blogs():
#     object1 = TestRTCBlogs()
#     object1.blogs_page_status()

from selenium import webdriver

driver = webdriver.Chrome()

class TestRTCBlogs:

    def blogs_page_status(self):

        base_url = "https://rtctek.com"

        driver.get(base_url)
        driver.maximize_window()

        # Click on Knowledge Center
        driver.find_element("xpath", "//a[text()='Knowledge Center']").click()

        # Get current URL after click
        current_url = driver.current_url
        print(f"Current URL: {current_url}")

        # Expected URL
        expected_url = base_url + "/blogs/"

        print(f"Expected URL: {expected_url}")

        # Assertion
        assert current_url == expected_url, f"URL mismatch: {current_url} != {expected_url}"


def test_RTC_blogs():
    obj = TestRTCBlogs()
    obj.blogs_page_status()