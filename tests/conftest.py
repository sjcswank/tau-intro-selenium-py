"""
This module contains shared fixtures
"""

import json
import pytest
import selenium.webdriver


@pytest.fixture
def config(scope="session"):

    # read the config file
    with open("config.json") as config_file:
        config = json.load(config_file)

    # assert values are acceptable
    assert config["browser"] in ["Chrome", "Firefox", "Headless Chrome"]
    assert isinstance(config["implicit_wait"], int)
    assert config["implicit_wait"] > 0

    # return the config for use
    return config


@pytest.fixture
def browser(config):

    # Initialize the webdriver instance
    if config["browser"] == "Chrome":
        b = selenium.webdriver.Chrome()
    elif config["browser"] == "Firefox":
        b = selenium.webdriver.Firefox()
    elif config["browser"] == "Headless Chrome":
        opt = selenium.webdriver.ChromeOptions()
        opt.add_argument("headless")
        b = selenium.webdriver.Chrome(options=opt)
    else:
        raise Exception(f'Broswer "{config["browser"]}" is not supported.')

    # Make WebDriver instance's calls wait for elements to appear
    b.implicitly_wait(config["implicit_wait"])

    # Return WebDriver instance for setup
    yield b

    # Quit WebDriver instance for cleanup
    b.quit()
