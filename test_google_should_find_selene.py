from selene.support.shared import browser
from selene import be, have


def test_positive(size_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_negative(size_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('qwqwqwqwqwqwqwqwqwqwqwqwqwdfdfdfdfdfdfdfdfdf').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
