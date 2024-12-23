from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

import time
import subprocess

# Global variable to hold the Appium session
appium_driver = None


def appium_start():
    global appium_driver

    if appium_driver is None:
        cap: Dict[str, Any] = {
            'platformName': 'Android',
            'automationName': 'uiautomator2'
        }

        url = 'http://127.0.0.1:4723'
        print("Starting Appium session...")
        appium_driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
        print("Appium session started:", appium_driver)
    else:
        print("Appium session already started:", appium_driver)

    return appium_driver


def appium_test1():
    print("Running test in appium_test1()")
    appium_driver = appium_start()
    # global appium_driver

    subprocess.check_output("adb shell am start -n com.android.settings/com.android.settings.Settings")

    network_and_internet = appium_driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                                      value='new UiSelector().text("Network & internet")')
    network_and_internet.click()
    time.sleep(2)

    airplane_mode = appium_driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                               value='new UiSelector().text("Airplane mode")')
    airplane_mode_switch = appium_driver.find_element(by=AppiumBy.ID, value='android:id/switch_widget')

    airplane_mode_state = airplane_mode_switch.get_attribute("checked")

    if airplane_mode_state == "false":
        print("Airplane mode off by default")
    else:
        print("Airplane mode on!!!!!!")


def appium_stop():
    global appium_driver
    if appium_driver is not None:
        print("Stopping Appium session...", appium_driver)
        appium_driver.quit()
        appium_driver = None
        print("Appium session stopped.")
    else:
        print("No Appium session to stop.")


# Example usage
# appium_start()
# appium_test1()
# appium_stop()

if __name__ == "__main__":
    appium_start()
    appium_test1()
    appium_stop()


# from appium import webdriver
# from typing import Any, Dict
# from appium.options.common import AppiumOptions
# from appium.webdriver.common.appiumby import AppiumBy
#
# import time
# import os
# import subprocess
#
# def appium_start():
#     cap: Dict[str, Any] = {
#         'platformName': 'Android',
#         'automationName': 'uiautomator2'
#     }
#
#     url = 'http://127.0.0.1:4723'
#     print("inside appium_start()")
#     appium_driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
#     print(appium_driver)
#     return appium_driver
#
#
# def appium_test1():
#     appium_driver = appium_start()
#     print(appium_driver)
#     print("inside appium_test1()")
#
#     subprocess.check_output("adb shell am start -n com.android.settings/com.android.settings.Settings")
#
#     network_and_internet = appium_driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
#                                                       value='new UiSelector().text("Network & internet")')
#     network_and_internet.click()
#     time.sleep(2)
#
#     airplane_mode = appium_driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
#                                                value='new UiSelector().text("Airplane mode")')
#     airplane_mode_switch = appium_driver.find_element(by=AppiumBy.ID, value='android:id/switch_widget')
#
#     airplane_mode_state = airplane_mode_switch.get_attribute("checked")
#
#     if airplane_mode_state == "false":
#         print("Airplane mode off by default")
#     else:
#         print("Airplane mode on!!!!!!")
#
#         # airplane_mode = appium_driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
#         #                                            value='new UiSelector().text("Airplane mode")')
#         # airplane_mode.click()
#
#     # appium_driver.quit()
#
#
# def appium_stop():
#     appium_driver = appium_start()
#     print(appium_driver)
#     print("inside appium_stop()")
#     appium_driver.quit()
#
#
# appium_start()
# appium_test1()
# appium_stop()
# # if __name__ == "__main__":
# #     appium_test()
