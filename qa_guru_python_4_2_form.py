from selene.support.shared import browser
from selene import be, have
import pytest
from selenium import webdriver


def test_form_1(browser_size_1680_1050):
#    browser.config.hold_browser_open = True

    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('[id=firstName]').type('Иван')
    browser.element('[id=lastName]').type('Иванов')
    browser.element('[id=userEmail]').type('qa_test@test.ru')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('[id=userNumber]').type('3334445555')

    # Choose Birthdate
    browser.element('[id=dateOfBirthInput]').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('option[value="7"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('option[value="2001"]').click()
    browser.element('[class="react-datepicker__day react-datepicker__day--029"]').click()

    browser.element('[id=subjectsInput]').type('Comm').element('//div[contains(text(),"Commerce")]').click()
    browser.element('[for=hobbies-checkbox-3]').click()
    browser.element('[id=uploadPicture]').send_keys('C:/Users/Hanna/Downloads/Без названия.jpg')

    browser.element('[id=currentAddress]').type("Планета Земля")
    browser.element('[id="submit"]').submit()

    # Inputs control
    browser.element('[id="example-modal-sizes-title-lg"]').should(have.text("Thanks"))
    browser.element('//tbody/tr[1]/td[2]').should(have.text("Иван Иванов"))
    browser.element('//tbody/tr[2]/td[2]').should(have.text("qa_test@test.ru"))
    browser.element('//tbody/tr[3]/td[2]').should(have.text("Male"))
    browser.element('//tbody/tr[4]/td[2]').should(have.text("3334445555"))
    browser.element('//tbody/tr[5]/td[2]').should(have.text("29 August,2001"))
    browser.element('//tbody/tr[6]/td[2]').should(have.text("Commerce"))
    browser.element('//tbody/tr[7]/td[2]').should(have.text("Music"))
    browser.element('//tbody/tr[9]/td[2]').should(have.text("Планета Земля"))

    browser.element('[id="closeLargeModal"]').click()
