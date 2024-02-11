"""
These tests cover DuckDuckGo searches
"""
import pytest

from pages.search import DuckDuckGoSearchPage
from pages.result import DuckDuckGoResultPage


@pytest.mark.parametrize("phrase", ["panda", "python", "polar bear"])
def test_basic_duckduckgo_search(browser, phrase):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)

    # Given the DuckDuckGo homepage is displayed
    search_page.load()

    # When the user searches phrase and hits enter
    search_page.enter_search_phrase(phrase)
    search_page.send_return_to_search()

    # Then the search result query is phrase
    assert phrase == result_page.search_input_value()

    # And the search result links pertain to phrase
    for title in result_page.result_link_titles():
        assert phrase.lower() in title.lower()

    # And the search result title contains phrase
    assert phrase in result_page.title()


@pytest.mark.parametrize("phrase", ["panda", "python", "polar bear"])
def test_search_by_button_click(browser, phrase):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)

    # Given the DuckDuckGo homepage is displayed
    search_page.load()

    # When the user searches phrase and clicks the search button
    search_page.enter_search_phrase(phrase)
    search_page.click_search_button()

    # Then the search result title contains phrase
    assert phrase in result_page.title()


def test_click_result_link(browser):
    result_page = DuckDuckGoResultPage(browser)

    # Given the DuckDuckGo result is displayed
    result_page.load()

    # When the user clicks on the first result
    result_page.click_result()

    # Then the current url does not contain DuckDuckGo
    assert "duckduckgo" not in result_page.current_url()


def test_click_more_results(browser):
    result_page = DuckDuckGoResultPage(browser)

    # Given the DuckDuckGo result page is displayed
    result_page.load()

    # When the user clicks the more results button
    result_page.click_more_results()

    # Then there are more than 10 results shown
    assert result_page.count_results() > 10


def test_autocomplete_contains_phrase(browser):
    result_page = DuckDuckGoResultPage(browser)

    # Given the DuckDuckGo result page is deisplayed
    result_page.load()

    # When the user clicks in the search input box
    result_page.click_search_input()

    # Then the autocomplete suggestions will pertain to the phrase
    for option in result_page.get_autocomplete_options():
        assert "panda" in option
