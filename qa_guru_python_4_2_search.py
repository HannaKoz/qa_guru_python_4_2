from selene import be, have
from selene.support.shared import browser


def test_search_1(browser_size_1280_920):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_search_2(browser_size_1680_1050):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('567777777777777755555555555ваваfghj').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_search_3(browser_size_1280_920):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('567777777777777755555555555ваваfghj').press_enter()
    browser.element('.card-section').should(have.text('ничего не найдено' or 'did not match any documents.'))
