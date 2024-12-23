# tests/conftest.py

import pytest
from config.appium_config import appium_start


@pytest.fixture(scope="function")
def appium_driver():
    driver = appium_start()
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def device_id1():
    return "my_device_serial"

@pytest.fixture(scope="session")
def device_id2():
    return "my_device_serial"

