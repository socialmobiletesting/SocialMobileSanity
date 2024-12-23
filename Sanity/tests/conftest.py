# tests/conftest.py

import pytest
from config.appium_config import appium_start


@pytest.fixture(scope="function")
def appium_driver():
    driver = appium_start()
    yield driver
    driver.quit()
