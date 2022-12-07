from selene.support.shared import browser
from selene import be, have


def test_positive():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in ...'))


def test_negative():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('qwqwqwqwqwqwqwqwqwqwqwqwqwdfdfdfdfdfdfdfdfdf').press_enter()
    browser.element('[role="heading"]').should(have.text('По запросу qwqwqwqwqwqwqwqwqwqwqwqwqwdfdfdfdfdfdfdfdfdf ничего не найдено.'))
