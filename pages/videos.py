"""
This module contains the page object
for the DuckDuckGo videos search page
"""

from selenium.webdriver.common.by import By


class DuckDuckGoVideosPage:

    def __init__(self, browser):
        self.browser = browser

