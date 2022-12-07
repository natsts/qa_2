from selene.support.shared import browser
import pytest

@pytest.fixture()
def size_browser():
    browser.config.window_width = 1000
    browser.config.window_height = 500