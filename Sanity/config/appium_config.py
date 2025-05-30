from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from Sanity.config.myconfig import data

# Global variable to hold the Appium session
appium_driver_1 = None
appium_driver_2 = None


def appium_start_1():
    global appium_driver_1

    if appium_driver_1 is None:
        cap: Dict[str, Any] = {
            'platformName': 'Android',
            'automationName': 'uiautomator2',
            'udid': data['device_id1']
        }

        url = 'http://127.0.0.1:4723'
        print("Starting Appium session...")
        appium_driver_1 = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
        print("Appium-1 session started:", appium_driver_1)
    else:
        print("Appium-1 session already started:", appium_driver_1)

    return appium_driver_1


def appium_start_2():
    global appium_driver_2

    if appium_driver_2 is None:
        cap: Dict[str, Any] = {
            'platformName': 'Android',
            'automationName': 'uiautomator2',
            'udid': data['device_id2']
        }

        url = 'http://127.0.0.1:4724'
        print("Starting Appium-2 session...")
        appium_driver_2 = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
        print("Appium-2 session started:", appium_driver_2)
    else:
        print("Appium-2 session already started:", appium_driver_2)

    return appium_driver_2


# def appium_stop_1():
#     global appium_driver_1
#     if appium_driver_1 is not None:
#         print("Stopping Appium-1 session...", appium_driver_1)
#         appium_driver_1.quit()
#         appium_driver_1 = None
#         print("Appium-1 session stopped.")
#     else:
#         print("No Appium-1 session to stop.")

