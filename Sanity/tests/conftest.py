import pytest
from Sanity.config.appium_config import appium_start


@pytest.fixture(scope="session")
def device_id1():
    return "090324127271"


@pytest.fixture(scope="session")
def device_id2():
    return "08SA23000010"


@pytest.fixture(scope="function")
def appium_driver1():
    driver = appium_start()
    yield driver
    # driver.quit()


@pytest.fixture(scope="function")
def appium_driver2(device_id2):
    """
    Fixture for Appium driver aligned with device_id2.
    """
    driver = appium_start(device_id=device_id2)
    yield driver
