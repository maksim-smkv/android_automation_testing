from src.helpers.init_config import InitConfig
from appium import webdriver
import pytest
import allure

desires_cap = {"deviceName": InitConfig.deviceName,
               "platformName": "Android",
               "autoGrantPermissions": "true",
               "appActivity": "some.application.mvp.login.LoginActivity",
               "app": InitConfig.app,
               "unicodeKeyboard": True,
               "resetKeyboard": True}

driver = webdriver.Remote(InitConfig.server, desires_cap)


@pytest.fixture(scope='session', autouse=True)
def init_driver(request):
    driver.implicitly_wait(5)
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", driver)

    yield
    driver.quit()


@pytest.fixture(scope="function")
def open_close_app_per_test():
    app_state = driver.query_app_state('some.application.debug')  # 1 - приложение закрыто, 4 - активно
    if app_state == 1 or app_state == 3:
        driver.launch_app()

    yield
    driver.close_app()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        try:
            allure.attach(driver.get_screenshot_as_png(),
                          name=item.name,
                          attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            print(e)
