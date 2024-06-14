import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
        help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
        help='Choose language: en, es, fr, etc.')
    parser.addoption('--sleep_time', action='store', default=0,
        help='Seconds sleep before exit')


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    user_language = request.config.getoption('language')
    sleep_time = request.config.getoption('sleep_time')
    if browser_name == "chrome":
        options = Options()
        options.headless = True
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print(f"\nsleep {sleep_time} seconds before browser.quit")
    time.sleep(int(sleep_time))
    if browser_name == "chrome":
        print("\ndelete chrome cookies...")
        browser.delete_all_cookies()
    print("\nquit browser..")
    browser.quit()
