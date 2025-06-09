import pytest
from Sanity.config.appium_config import appium_start_1, appium_start_2
from Sanity.config.myconfig import data
import inspect
import os
import subprocess
from datetime import datetime

log_process_dict = {}


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


def screenshot_device1():
    try:
        # Get the name of the test function that called this
        calling_function = inspect.stack()[1].function

        # Get build version dynamically
        build_version = subprocess.check_output(
            f"adb -s {data["device_id1"]} shell getprop ro.build.display.id", shell=True, text=True
        ).strip()

        # Create screenshot folder
        screenshot_folder = os.path.join(os.path.dirname(os.getcwd()), "Screenshot", build_version)
        os.makedirs(screenshot_folder, exist_ok=True)

        # Define screenshot name
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_name = f"{calling_function}_{timestamp}.png"
        local_path = os.path.join(screenshot_folder, screenshot_name)

        # Capture screenshot using adb exec-out
        with open(local_path, "wb") as f:
            subprocess.run(
                ["adb", "-s", data["device_id1"], "exec-out", "screencap", "-p"],
                stdout=f,
                check=True
            )

        print(f"[SUCCESS] Screenshot saved at: {local_path}")
        return local_path

    except Exception as e:
        print(f"[ERROR] Unexpected error at screenshot_device1: {e}")


def start_adb_log_capture1():
    try:
        calling_function = inspect.stack()[1].function
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        log_folder = os.path.join(os.path.dirname(os.getcwd()), "Logs")
        os.makedirs(log_folder, exist_ok=True)

        log_filename = f"{data["device_id1"]}_{calling_function}_{timestamp}.log"
        log_path = os.path.join(log_folder, log_filename)

        with open(log_path, "wb") as log_file:
            log_proc = subprocess.Popen(
                ["adb", "-s", data["device_id1"], "logcat"],
                stdout=log_file,
                stderr=subprocess.STDOUT
            )
            log_process_dict[data["device_id1"]] = (log_proc, log_path)

        print(f"[STARTED] ADB log for {data["device_id1"]} -> {log_path}")
        return log_path
    except Exception as e:
        print(f"[ERROR] Unexpected error at start_adb_log_capture1: {e}")


def stop_adb_log_capture1():
    try:
        if data["device_id1"] in log_process_dict:
            log_proc, log_path = log_process_dict[data["device_id1"]]
            log_proc.terminate()
            log_proc.wait()
            print(f"[STOPPED] ADB log {data["device_id1"]} saved: {log_path}")
            del log_process_dict[data["device_id1"]]
        else:
            print(f"[WARN] No running ADB log capture found for {data["device_id1"]}")
    except Exception as e:
        print(f"[ERROR] Unexpected error at stop_adb_log_capture1: {e}")
