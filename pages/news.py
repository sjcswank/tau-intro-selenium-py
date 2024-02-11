"""
This module contains the page object
for the DuckDuckGo news search page
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class DuckDuckGoNewsPage:

    URL = "https://duckduckgo.com/?q=panda&t=h_&iar=news&ia=news"
    SEARCH_INPUT = (By.ID, "search_form_input")
    RESULT_LINKS = (By.CLASS_NAME, "result__a")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def new_search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(phrase + Keys.RETURN)

    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        value = search_input.get_attribute("value")
        return value

    def title(self):
        return self.browser.title

    def result_link_titles(self):
        links = self.browser.find_elements(*self.RESULT_LINKS)
        titles = [link.text for link in links]
        return titles

