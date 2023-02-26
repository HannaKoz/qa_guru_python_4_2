from selene.support.shared import browser
from selene import be, have
import pytest
from selenium import webdriver

@pytest.fixture()
def browser_size_1280_920():
    browser.config.window_width = 1280
    browser.config.window_height = 920

@pytest.fixture()
def browser_size_1680_1050():
    browser.config.window_width = 1680
    browser.config.window_height = 1050
    yield browser_size_1680_1050
    browser.config.hold_browser_open = True