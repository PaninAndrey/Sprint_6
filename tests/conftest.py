import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from curl import *


# Фикстура для запуска браузера и закрытия окна
# браузера после выполнения теста

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--window-size=1200,600")
    browser = webdriver.Firefox(options=options)
    browser.get(main_site)
    yield browser
    browser.quit()
