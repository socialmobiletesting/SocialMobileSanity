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
    # print("Unlocking device...")
    subprocess.check_output("adb -s " + "08RSA23123505" + " shell input keyevent 82", shell=True)

    # print("Navigating to 'Network and Internet' > 'SIMs' > 'JIO'...")
    subprocess.check_output("adb -s " + "08RSA23123505" + " shell am start -n com.android.settings/com.android.settings.Settings")

    network_and_internet = appium_driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                                  value='new UiSelector().text("Network and internet")')
    network_and_internet.click()
    time.sleep(2)

    click_on_sim = appium_driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("SIMs")')
    click_on_sim.click()

    navigate_into_sim = appium_driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().resourceId("android:id/summary")')
    navigate_into_sim.click()

    check_roaming_option = appium_driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Roaming"))')
    check_roaming_switch = appium_driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                                      value='new UiSelector().resourceId("android:id/switch_widget").instance(2)')

    check_roaming_state = check_roaming_switch.get_attribute("checked")

    if check_roaming_state == "false":
        print("Roaming off !!!!!!")
    else:
        print("Roaming is on")

    subprocess.check_output(
        "adb shell am force-stop com.android.settings")

appium_start()
appium_test1()
