import pytest
from Sanity.config.appium_config import appium_start_1, appium_start_2
from Sanity.config.myconfig import data


@pytest.fixture(scope="session")
def device_id1():
    return data['device_id1']


@pytest.fixture(scope="session")
def device_id2():
    return data['device_id2']


@pytest.fixture(scope="function")
def appium_driver1():
    driver1 = appium_start_1()
    yield driver1
    # driver.quit()


@pytest.fixture(scope="function")
def appium_driver2():
    driver2 = appium_start_2()
    yield driver2


@pytest.fixture(scope="session")
def device_id1_number():
    return data['device_id1_number']


@pytest.fixture(scope="session")
def device_id2_number():
    return data['device_id2_number']