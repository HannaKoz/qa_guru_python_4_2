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

def test_search_1(browser_size_1280_920):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_search_2(browser_size_1680_1050):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('567777777777777755555555555').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_search_3(browser_size_1280_920):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('567777777777777755555555555').press_enter()
    browser.element('.card-section').should(have.text('ничего не найдено' or 'did not match any documents.'))
