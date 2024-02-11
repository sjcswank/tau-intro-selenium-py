"""
This module contains the page object for
the DuckDuckGo image search page
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class DuckDuckGoImagesPage:
    URL = "https://duckduckgo.com/?t=h_&q=panda&iax=images&ia=images"
    SEARCH_INPUT = (By.ID, "search_form_input")
    IMAGE_LINKS = (By.CLASS_NAME, "tile--img__sub")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def new_search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(phrase + Keys.RETURN)

    def title(self):
        return self.browser.title

    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        value = search_input.get_attribute("value")
        return value

    def image_link_titles(self):
        image_links = self.browser.find_elements(*self.IMAGE_LINKS)
        titles = [link.text for link in image_links]
        return titles
