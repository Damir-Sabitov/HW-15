import pytest
from selene import browser, have


@pytest.fixture (params=[(844,390),(414,896),(430,932),(1920, 1080), (2560, 1440), (2000, 1200),(600,840)])
def size(request):
    browser.config.window_width, browser.config.window_height = request.param
    yield 'desktop' if browser.config.window_width > 1011 else 'mobile'
    browser.quit()


def test_mobile_skip(size):
    if size == "mobile":
        pytest.skip(reason="Skipping mobile tests")

    browser.open('https://github.com')
    browser.element('.HeaderMenu-link--sign-up').click()
    browser.element('html').should(have.text('Sign up for GitHub'))

def test_desktop_skip(size):
    if size == "desktop":
        pytest.skip(reason="Skipping desktop tests")

    browser.open('https://github.com')
    browser.element('.js-header-menu-toggle').click()
    browser.element('.HeaderMenu-link--sign-up').click()
    browser.element('html').should(have.text('Sign up for GitHub'))




