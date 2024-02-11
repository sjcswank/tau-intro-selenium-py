"""
This module contains the page object for the
DuckDuckGo search results page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class DuckDuckGoResultPage:
    URL = "https://duckduckgo.com/?t=h_&q=panda&ia=web"
    RESULT_LINKS = (By.CLASS_NAME, "eVNpHGjtxRBq_gLOfGDr")
    SEARCH_INPUT = (By.ID, "search_form_input")
    MORE_RESULTS = (By.ID, "more-results")
    AUTO_COMPLETE = (By.CSS_SELECTOR, 'div[role="option"]')
    IMAGES_LINK = (By.LINK_TEXT, "Images")
    VIDEO_LINK = (By.LINK_TEXT, "Videos")
    NEWS_LINK = (By.LINK_TEXT, "News")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def result_link_titles(self):
        links = self.browser.find_elements(*self.RESULT_LINKS)
        titles = [link.text for link in links]
        return titles

    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        value = search_input.get_attribute("value")
        return value

    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)

    def title(self):
        return self.browser.title

    def click_result(self):
        links = self.browser.find_elements(*self.RESULT_LINKS)
        links[0].click()

    def current_url(self):
        return self.browser.current_url

    def click_more_results(self):
        more_results = self.browser.find_element(*self.MORE_RESULTS)
        more_results.click()

    def count_results(self):
        results = self.browser.find_elements(*self.RESULT_LINKS)
        return len(results)

    def autocomplete_options(self):
        auto_complete = self.browser.find_elements(*self.AUTO_COMPLETE)
        options = [option.text for option in auto_complete]
        return options

    def click_search_input(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.click()
