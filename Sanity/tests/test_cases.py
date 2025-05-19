import subprocess
import time

from appium.webdriver.common.appiumby import AppiumBy


def test_sample(appium_driver1, device_id1):
    subprocess.check_output("adb -s " + device_id1 + " shell am force-stop com.android.settings", shell=True)
    time.sleep(5)

    subprocess.check_output(
        "adb -s " + device_id1 + " shell am start -n com.android.settings/com.android.settings.Settings", shell=True)
    time.sleep(10)

    network_and_internet = appium_driver1.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                                      value='new UiSelector().text("Network & internet")')
    network_and_internet.click()
    time.sleep(2)

    airplane_mode = appium_driver1.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                               value='new UiSelector().text("Airplane mode")')
    airplane_mode_switch = appium_driver1.find_element(by=AppiumBy.ID, value='android:id/switch_widget')

    airplane_mode_state = airplane_mode_switch.get_attribute("checked")

    if airplane_mode_state == "false":
        print("Airplane mode off by default")
    else:
        print("Airplane mode on!!!!!!")

    time.sleep(5)


def test_notification_panel_working_fine(appium_driver1, device_id1):
    print("=====================test_notification_panel_working_fine()")

    output = subprocess.check_output("adb -s " + device_id1 + " shell wm size", shell=True)
    # print(output.decode("utf-8"))

    resolution = output.decode("utf-8")
    _, custom_resolution = resolution.split(": ")
    # print(custom_resolution)
    width, height = custom_resolution.split("x")
    x_axis = int(width)
    y_axis = int(height)
    half_x_axis = x_axis / 2
    half_y_axis = y_axis / 2
    str_x_axis = str(int(half_x_axis))
    str_y_axis = str(int(half_y_axis))
    # print(str_x_axis)
    # print(half_y_axis)

    subprocess.check_output(
        "adb -s " + device_id1 + " shell input swipe " + str_x_axis + " 0 " + str_x_axis + " " + str_y_axis, shell=True)

    # screenshot_capture()
    try:
        # Get build version dynamically
        build_version = subprocess.check_output(["adb " + device_id1 + " shell", "getprop", "ro.build.display.id"],
                                                text=True).strip()
        screenshot_folder = os.path.join(os.path.dirname(os.getcwd()), "Screenshot", build_version)
        # print(screenshot_folder)

        # Define screenshot name
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_name = f"{inspect.stack()[1].function}_{timestamp}.png"
        local_path = os.path.join(screenshot_folder, screenshot_name)

        # Capture screenshot using ADB
        device_screenshot_path = f"/sdcard/{screenshot_name}"
        subprocess.run(["adb", " -s " + device_id1 + " shell ", "screencap", " -p ", device_screenshot_path],
                       check=True)

        # Pull screenshot to local path
        subprocess.run(["adb", " -s " + device_id1 + " pull ", device_screenshot_path, local_path], check=True)

        # Delete screenshot from device
        subprocess.run(["adb", " -s " + device_id1 + " shell ", "rm ", device_screenshot_path], check=True)

        print(f"Screenshot saved at: {local_path}")
        return local_path
    except Exception as e:
        print(f"Unexpected error: {e}")

    time.sleep(5)


def test_verify_apn_is_loaded_automatically(appium_driver1, device_id1):
    print("=====================test_verify_apn_is_loaded_automatically()")
    subprocess.check_output("adb -s " + device_id1 + " shell am force-stop com.android.settings", shell=True)
    time.sleep(5)

    subprocess.check_output("adb -s " + device_id1 + " shell am force-stop com.android.settings", shell=True)
    time.sleep(5)

    subprocess.check_output("adb -s " + device_id1 + " shell input keyevent KEYCODE_HOME")

    subprocess.check_output(
        "adb -s " + device_id1 + " shell am start -n com.android.settings/com.android.settings.Settings", shell=True)
    time.sleep(10)

    appium_driver1.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                value='new UiSelector().text("Network & internet")').click()
    # network_and_internet = appium_driver.find_element(AppiumBy.XPATH, '//android.widget.TextView['
    #                                                                   '@resource-id="android:id/title" and '
    #                                                                   '@text="Network & internet"]').click()
    time.sleep(2)

    sims_option = appium_driver1.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("SIMs")')
    sims_option.click()
    time.sleep(2)

    try:
        active_sim = appium_driver1.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                 'new UiSelector().resourceId("android:id/summary")')
        active_sim_state = active_sim.get_attribute("text")
        time.sleep(2)
        if active_sim_state == "Active / Default for mobile data, calls, SMS":
            appium_driver1.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                        'new UiSelector().resourceId("android:id/summary")').click()
            # print("scrolling and clicking Access Point Name")
            appium_driver1.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                        'new UiScrollable(new UiSelector().scrollable(true))'
                                        '.scrollIntoView(new UiSelector().text("Access Point Names"))').click()
            time.sleep(2)

            apn_name = appium_driver1.find_element(AppiumBy.ID, 'android:id/title')
            get_apn_name = apn_name.get_attribute("text")
            print("APN name is : ", get_apn_name)

            # print("checking apn names")
            apn_details = appium_driver1.find_element(AppiumBy.ID, 'android:id/title')
            apn_state = apn_details.get_attribute("enabled")
            time.sleep(2)

            # print("validation part")
            if apn_state == "true":
                print("default apn is enabled")
            else:
                print("apn not enabled")
    except Exception as e:
        print("SIM Card not detected", e)
    time.sleep(5)


def test_verify_data_roaming_works(appium_driver1, device_id1):
    print("=====================test_verify_data_roaming_works()")
    subprocess.check_output("adb -s " + device_id1 + " shell am force-stop com.android.settings", shell=True)
    time.sleep(5)

    # print("Navigating to 'Network and Internet' > 'SIMs' > 'JIO'...")
    subprocess.check_output(
        "adb -s " + device_id1 + " shell am start -n com.android.settings/com.android.settings.Settings")
    time.sleep(10)

    appium_driver1.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                value='new UiSelector().text("Network & internet")').click()

    time.sleep(2)

    click_on_sim = appium_driver1.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("SIMs")')
    click_on_sim.click()
    time.sleep(2)

    appium_driver1.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                value='new UiSelector().resourceId("android:id/summary")').click()
    # navigate_into_sim.click()
    time.sleep(2)

    check_roaming_option = appium_driver1.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                                       value='new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Roaming"))')
    check_roaming_switch = appium_driver1.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                                       value='new UiSelector().resourceId("android:id/switch_widget").instance(2)')

    check_roaming_state = check_roaming_switch.get_attribute("checked")

    if check_roaming_state != "true":
        print("Roaming is not enabled!")
        print(f"Actual state: {check_roaming_state}")
        assert False, "Test failed due to roaming not being enabled."

    # If Roaming is enabled, print success
    print("Roaming is enabled as expected.")

    time.sleep(5)


def test_check_lte_data_speed(appium_driver1, device_id1):
    print("=====================test_check_lte_data_speed()")

    # Defined this condition due to PlayStore Home Page tutorial, which can be skipped by re-opening
    max_retries = 5
    count = 0
    while count <= max_retries:
        try:
            subprocess.check_output(
                "adb -s " + device_id1 + " shell am start -n com.android.vending/com.google.android.finsky.activities.MainActivity")
            time.sleep(10)
            playstore_app_tutorial_1 = appium_driver1.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                                 value='new UiSelector().text("Search")')
            time.sleep(2)

            if playstore_app_tutorial_1.is_displayed():
                playstore_app_tutorial_1.click()
                break
            else:
                subprocess.check_output(
                    "adb -s " + device_id1 + " shell pm clear com.android.vending")
                time.sleep(10)
                subprocess.check_output(
                    "adb -s " + device_id1 + " shell am start -n com.android.vending/com.google.android.finsky.activities.MainActivity")
                time.sleep(10)

        except Exception as e:
            print(f"Search bar not visible, clearing Play Store data and retrying ({count + 1}/{max_retries})")
        count = count+1

    search_ookla_app = appium_driver1.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                                 value='new UiSelector().text("Search Apps & Games")')
    search_ookla_app.click()
    time.sleep(2)

    search_ookla_app_1 = appium_driver1.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
    search_ookla_app_1.send_keys("ookla")
    time.sleep(2)

    search_ookla_app_2 = appium_driver1.find_element(by=AppiumBy.ACCESSIBILITY_ID,
                                                   value="Search for 'ookla' ")
    search_ookla_app_2.click()
    time.sleep(2)

    install_ookla_app = (appium_driver1.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().className("android.widget.Button").instance(1)'))
    install_ookla_app.click()
    time.sleep(30)

    subprocess.check_output(
        "adb -s " + device_id1 + " shell am start -n org.zwanoo.android.speedtest/com.ookla.mobile4.screens.main.MainActivity")
    time.sleep(10)

    try:
        app_tutorial_1 = appium_driver1.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                                         value='new UiSelector().resourceId("org.zwanoo.android.speedtest:id/welcome_message_next_button")')
        app_tutorial_1.click()
        time.sleep(2)

        app_tutorial_2 = appium_driver1.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                                         value='new UiSelector().resourceId("org.zwanoo.android.speedtest:id/permissions_continue_button")')
        app_tutorial_2.click()
        time.sleep(2)

        user_location_permission = appium_driver1.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                                     value='new UiSelector().resourceId("com.android.permissioncontroller:id/permission_allow_foreground_only_button")')
        user_location_permission.click()
        time.sleep(2)

        user_call_permission = appium_driver1.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                                               value='new UiSelector().resourceId("com.android.permissioncontroller:id/permission_allow_button")')
        user_call_permission.click()
        time.sleep(2)

        app_own_permission_1 = appium_driver1.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                                           value='new UiSelector().resourceId("org.zwanoo.android.speedtest:id/enable_bg_sampling_allow_button")')
        app_own_permission_1.click()
        time.sleep(2)

        app_own_permission_2 = appium_driver1.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                                           value='new UiSelector().resourceId("org.zwanoo.android.speedtest:id/dialog_next")')
        app_own_permission_2.click()
        time.sleep(2)

        app_own_permission_3 = appium_driver1.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                                           value='new UiSelector().description("Navigate up")')
        app_own_permission_3.click()
        time.sleep(2)

        app_own_permission_4 = appium_driver1.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                                           value='new UiSelector().resourceId("org.zwanoo.android.speedtest:id/btn_accept_cookies")')
        app_own_permission_4.click()
        time.sleep(2)
    except Exception as e:
        print("Something wrong while accepting permissions", e)

    initiating_test = appium_driver1.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                                       value='new UiSelector().resourceId("org.zwanoo.android.speedtest:id/go_button")')
    initiating_test.click()
    time.sleep(30)

