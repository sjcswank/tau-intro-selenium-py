"""
This module contains the page object for the
DuckDuckGo search results page.
"""

from selenium.webdriver.common.by import By


class DuckDuckGoResultPage:

    RESULT_LINKS = (By.CLASS_NAME, "eVNpHGjtxRBq_gLOfGDr")
    SEARCH_INPUT = (By.ID, "search_form_input")

    def __init__(self, browser):
        self.browser = browser

    def result_link_titles(self):
        links = self.browser.find_elements(*self.RESULT_LINKS)
        titles = [link.text for link in links]
        return titles

    def search_input_value(self):
        search_input_value = self.browser.find_element(*self.SEARCH_INPUT)
        value = search_input_value.get_attribute("value")
        return value

    def title(self):
        return self.browser.title

    def click_result(self):
        links = self.browser.find_elements(*self.RESULT_LINKS)
        links[0].click()

    def current_url(self):
        return self.browser.current_url
