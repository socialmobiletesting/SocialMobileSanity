from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

import time
import subprocess

# Global variable to hold the Appium session
appium_driver_1 = None


def appium_start_1():
    global appium_driver_1

    if appium_driver_1 is None:
        cap: Dict[str, Any] = {
            'platformName': 'Android',
            'automationName': 'uiautomator2'
        }

        url = 'http://127.0.0.1:4723'
        print("Starting Appium session...")
        appium_driver_1 = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
        print("Appium-1 session started:", appium_driver_1)
    else:
        print("Appium-1 session already started:", appium_driver_1)

    return appium_driver_1


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


def appium_stop_1():
    global appium_driver_1
    if appium_driver_1 is not None:
        print("Stopping Appium session...", appium_driver_1)
        appium_driver_1.quit()
        appium_driver_1 = None
        print("Appium-1 session stopped.")
    else:
        print("No Appium-1 session to stop.")


# Example usage
# appium_start()
# appium_test1()
# appium_stop()

if __name__ == "__main__":
    appium_start_1()
    appium_test1()
    appium_stop_1()


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
