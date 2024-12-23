import subprocess
import time

from appium.webdriver.common.appiumby import AppiumBy


# from appium.webdriver.common.actions.action_builder import ActionBuilder
# from appium.webdriver.common.actions.pointer_input import PointerInput, PointerEvent


# def test_sample(appium_driver):
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
#
# def test_notification_panel_working_fine(appium_driver):
#     print("Hello")
#
#     # get screen size
#     screen_size = appium_driver.get_window_size()
#     width = screen_size['width']
#     height = screen_size['height']
#
#     # Starting point (top of the screen)
#     start_x = width / 2
#     start_y = height * 0.1  # Near the top edge
#
#     # Ending point (middle of the screen)
#     end_x = width / 2
#     end_y = height * 0.5  # Move to the middle of the screen
#
#     actions = TouchAction(appium_driver)
#     actions.press(x=start_x, y=start_y).wait(1000).move_to(x=end_x, y=end_y).release().perform()


def test_verify_apn_is_loaded_automatically(appium_driver):
    # print("Unlocking device...")
    subprocess.check_output("adb shell input keyevent 82", shell=True)

    # print("Navigating to 'Network and Internet' > 'SIMs' > 'JIO'...")
    subprocess.check_output(
        "adb shell am start -n com.android.settings/com.android.settings.Settings")

    network_and_internet = appium_driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                                      value='new UiSelector().text("Network and internet")')
    network_and_internet.click()
    time.sleep(2)

    click_on_sim = appium_driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("SIMs")')
    click_on_sim.click()

    appium_driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                                   value='new UiSelector().resourceId("android:id/summary")').click()
    # navigate_into_sim.click()

    check_roaming_option = appium_driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                                      value='new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Roaming"))')
    check_roaming_switch = appium_driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                                   value='new UiSelector().resourceId("android:id/switch_widget").instance(2)')

    check_roaming_state = check_roaming_switch.get_attribute("checked")

    if check_roaming_state != "true":
        print("Roaming is not enabled!")
        print(f"Actual state: {check_roaming_state}")
        assert False, "Test failed due to roaming not being enabled."

    # If Roaming is enabled, print success
    print("Roaming is enabled as expected.")

    subprocess.check_output("adb shell am force-stop com.android.settings", shell=True)


# def test_appium_stopping():
#     appium_stop()
