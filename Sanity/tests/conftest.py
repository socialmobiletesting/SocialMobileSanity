import pytest
from Sanity.config.appium_config import appium_start_1, appium_start_2
from Sanity.config.myconfig import data


@pytest.fixture(scope="function")
def appium_driver1():
    driver1 = appium_start_1()
    yield driver1
    # driver.quit()


@pytest.fixture(scope="function")
def appium_driver2():
    driver2 = appium_start_2()
    yield driver2


@pytest.fixture()
def data_file():
    return data
