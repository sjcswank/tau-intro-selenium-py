"""
This module contains the page object for the
DuckDuckGo search page
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class DuckDuckGoSearchPage:

    URL = "https://duckduckgo.com/"
    SEARCH_INPUT = (By.ID, "searchbox_input")
    SEARCH_BUTTON = (By.CLASS_NAME, "searchbox_searchButton__F5Bwq")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def enter_search_phrase(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase)

    def send_return_to_search(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(Keys.RETURN)

    def click_search_button(self):
        search_button = self.browser.find_element(*self.SEARCH_BUTTON)
        search_button.click()
