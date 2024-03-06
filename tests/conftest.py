import pytest
from utils import attach
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function", autouse=True)
def browser_config():

    browser.config.base_url = 'https://demoqa.com/'
    browser.config.window_height = 1080
    browser.config.window_width = 1920

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )
    browser.config.driver = driver

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
