import pytest
from selenium import webdriver
import datetime

import os

driver = None


@pytest.fixture()
def setup(request):
    global driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.addfinalizer(lambda: driver.quit())
    return driver


REPORT_PATH = "D:\\Automation\\PythonAutomation\\minopcloud\\pythonProject\\Reports\\"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call":
        feature_request = item.funcargs['request']
        driver = feature_request.getfixturevalue('setup')
        nodeid = item.nodeid

        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = f'{nodeid}_{datetime.datetime.now().strftime("%Y-%m-%d_%H_%M")}.png'.replace("/", "_").replace("::", "_").replace(".py", "")
            img_path = os.path.join(REPORT_PATH, "ScreenShots", file_name)
            driver.save_screenshot(img_path)
            screenshot = driver.get_screenshot_as_base64()
            extra.append(pytest_html.extras.image(screenshot, ''))

    report.extra = extra


