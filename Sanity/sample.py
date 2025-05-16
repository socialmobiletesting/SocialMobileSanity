from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

import time
import subprocess

# Global variable to hold the Appium session
appium_driver1 = None


def appium_start():
    global appium_driver1

    if appium_driver1 is None:
        cap: Dict[str, Any] = {
            'platformName': 'Android',
            'automationName': 'uiautomator2',
            'browserName': 'Chrome',
            'chromedriverExecutable': 'C:\\Dropbox\\Tools\\Google\\chromedriver-win64\\chromedriver'
        }

        url = 'http://127.0.0.1:4723'
        print("Starting Appium session...")
        appium_driver1 = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
        print("Appium session started:", appium_driver1)
    else:
        print("Appium session already started:", appium_driver1)

    return appium_driver1


def appium_test1():
    # print("Unlocking device...")
    subprocess.check_output("adb -s " + "08RSA23123505" + " shell input keyevent 82", shell=True)

    appium_driver1.get("https://www.fast.com")
    time.sleep(15)  # Wait for the speed to load
    speed_value = appium_driver1.find_element(AppiumBy.XPATH, "//div[@id='speed-value']").text
    print(speed_value)


# Global variable to hold the Appium session
appium_driver2 = None


def appium_start_device2():
    global appium_driver2

    if appium_driver2 is None:
        cap: Dict[str, Any] = {
            'platformName': 'Android',
            'automationName': 'uiautomator2',
            'browserName': 'Chrome',
            'chromedriverExecutable': 'C:\\Dropbox\\Tools\\Google\\chromedriver-win64\\chromedriver'
        }

        url = 'http://127.0.0.1:4723'
        print("Starting Appium session...")
        appium_driver2 = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
        print("Appium session started:", appium_driver2)
    else:
        print("Appium session already started:", appium_driver2)

    return appium_driver2


def appium_test1_device2():
    # print("Unlocking device...")
    subprocess.check_output("adb -s " + "08SA23000010" + " shell input keyevent 82", shell=True)

    appium_driver2.get("https://www.fast.com")
    time.sleep(15)  # Wait for the speed to load
    speed_value = appium_driver2.find_element(AppiumBy.XPATH, "//div[@id='speed-value']").text
    print(speed_value)



appium_start()
appium_test1()
appium_start_device2()
appium_test1_device2()