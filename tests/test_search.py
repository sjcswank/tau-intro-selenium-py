"""
These tests cover DuckDuckGo searches
"""
import pytest

from pages.search import DuckDuckGoSearchPage
from pages.result import DuckDuckGoResultPage
from pages.images import DuckDuckGoImagesPage
from pages.videos import  DuckDuckGoVideosPage
from pages.news import DuckDuckGoNewsPage


# @pytest.mark.parametrize("phrase", ["panda", "python", "polar bear"])
# def test_basic_duckduckgo_search(browser, phrase):
#     search_page = DuckDuckGoSearchPage(browser)
#     result_page = DuckDuckGoResultPage(browser)
#
#     # Given the DuckDuckGo homepage is displayed
#     search_page.load()
#
#     # When the user searches phrase and hits enter
#     search_page.enter_search_phrase(phrase)
#     search_page.send_return_to_search()
#
#     # Then the search result query is phrase
#     assert phrase == result_page.search_input_value()
#
#     # And the search result links pertain to phrase
#     for title in result_page.result_link_titles():
#         assert phrase.lower() in title.lower()
#
#     # And the search result title contains phrase
#     assert phrase in result_page.title()
#
#
# @pytest.mark.parametrize("phrase", ["panda", "python", "polar bear"])
# def test_search_by_button_click(browser, phrase):
#     search_page = DuckDuckGoSearchPage(browser)
#     result_page = DuckDuckGoResultPage(browser)
#
#     # Given the DuckDuckGo homepage is displayed
#     search_page.load()
#
#     # When the user searches phrase and clicks the search button
#     search_page.enter_search_phrase(phrase)
#     search_page.click_search_button()
#
#     # Then the search result title contains phrase
#     assert phrase in result_page.title()
#
#
# def test_click_result_link(browser):
#     result_page = DuckDuckGoResultPage(browser)
#
#     # Given the DuckDuckGo result is displayed
#     result_page.load()
#
#     # When the user clicks on the first result
#     result_page.click_result()
#
#     # Then the current url does not contain DuckDuckGo
#     assert "duckduckgo" not in result_page.current_url()
#
#
# def test_click_more_results(browser):
#     result_page = DuckDuckGoResultPage(browser)
#
#     # Given the DuckDuckGo result page is displayed
#     result_page.load()
#
#     # When the user clicks the more results button
#     result_page.click_more_results()
#
#     # Then there are more than 10 results shown
#     assert result_page.count_results() > 10
#
#
# def test_autocomplete_contains_phrase(browser):
#     result_page = DuckDuckGoResultPage(browser)
#
#     # Given the DuckDuckGo result page is deisplayed
#     result_page.load()
#
#     # When the user clicks in the search input box
#     result_page.click_search_input()
#
#     # Then the autocomplete suggestions will pertain to the phrase
#     for option in result_page.get_autocomplete_options():
#         assert "panda" in option
#
#
# def test_autocomplete_search(browser):
#     search_page = DuckDuckGoSearchPage(browser)
#     result_page = DuckDuckGoResultPage(browser)
#
#     # Given the DuckDuckGo search page is loaded
#     search_page.load()
#
#     # When the user enters a search term
#     search_page.enter_search_phrase("p")
#
#     # And the user clicks on the first autocomplete suggestion
#     autocomplete_suggestion = search_page.get_autocomplete_suggestion_text()
#     search_page.click_autocomplete_suggestion()
#
#     # Then the search result title contains autocomplete suggestion
#     assert autocomplete_suggestion in result_page.title()
#
#
# def test_search_from_result_page(browser):
#     result_page = DuckDuckGoResultPage(browser)
#
#     # Given the result page is loaded
#     result_page.load()
#
#     # When the user searches for a new phrase
#     result_page.search("python")
#
#     # Then the result page title contains the new phrase
#     assert "python" in result_page.title()
#
#
# def test_image_search(browser):
#     image_page = DuckDuckGoImagesPage(browser)
#
#     # Given the image search page is loaded
#     image_page.load()
#
#     # When the user searches for a new phrase
#     image_page.new_search("python")
#
#     # Then the search result query is the new phrase
#     assert "python" == image_page.search_input_value()
#
#     # And the search result title contains the new phrase
#     assert "python" in image_page.title()
#
#     # # And the image link titles will pertain to the new phrase
#     # for title in image_page.image_link_titles():
#     #     assert "python" in title.lower()
#
#     # TODO Add visual tests to image page?
#
#
# def test_videos_search(browser):
#     videos_page = DuckDuckGoVideosPage(browser)
#
#     # Given the video search page is loaded
#     videos_page.load()
#
#     # When the user searches for a new phrase
#     videos_page.new_search("python")
#
#     # Then the search result query is the new phrase
#     assert "python" == videos_page.search_input_value()
#
#     # And the search result title contains the new phrase
#     assert "python" in videos_page.title()
#
#     # And the videos will pertain to the new phrase
#
#     # TODO Add visual tests to videos page?

def test_news_search(browser):
    news_page = DuckDuckGoNewsPage(browser)

    # Given the news search page is loaded
    news_page.load()

    # When the user searches for a new phrase
    news_page.new_search("python")

    # Then the search result query is the new phrase
    assert "python" == news_page.search_input_value()

    # And the search result title contains the new phrase
    assert "python" in news_page.title()

    # And the news result titles pertain to the new phrase
    for title in news_page.result_link_titles():
        assert "python" in title.lower()