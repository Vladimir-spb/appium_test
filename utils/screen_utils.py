import datetime
from pathlib import Path

from driver.browser import Application
from element.base_element import BaseElementClass

SCREENSHOT_DIR = Path(__file__).parent.parent


class ScreenshotUtils:

    @staticmethod
    def take_app_screenshot():

        file_path = f"{SCREENSHOT_DIR}\\screen\\{datetime.datetime.today().strftime('%Y-%m-%d_%H_%M_%S')}.png"
        Application().driver.save_screenshot(file_path)
        return file_path

    @staticmethod
    def take_element_screenshot(element: BaseElementClass):
        element_name = element.get_name()
        file_path = f"{SCREENSHOT_DIR}\\screen\\{datetime.datetime.today().strftime(f'{element_name}_%Y-%m-%d_%H_%M_%S')}.png"
        element.find_element().screenshot(file_path)
        return file_path
