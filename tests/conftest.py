"""
This module contains shared fixtures
"""

import pytest
import selenium.webdriver


@pytest.fixture
def browser():
    # Initialize the ChromeDriver instance
    b = selenium.webdriver.Chrome()

    # Make its calls wait up to 10 seconds for elements to appear
    b.implicitly_wait(10)

    # Return WebDriver instance for setup
    yield b

    # Quit WebDriver instance for cleanup
    b.quit()
