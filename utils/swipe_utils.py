from enum import Enum

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains

from driver.browser import Application


class SwipeDirection(Enum):
    DOWN = 'down'
    UP = 'up'
    LEFT = 'left'
    RIGHT = 'right'


class SwipeUtils:
    ANIMATION_TIME = 3  # sec
    PRESS_TIME = 3  # sec
    EDGE_BORDER = 30  # px

    @staticmethod
    def get_dimensions() -> tuple:
        dimensions = Application().driver.get_window_size()
        width = dimensions.get("width")
        height = dimensions.get("height")
        return width, height

    @staticmethod
    def swipe_by_coordinates(start_x: int, start_y: int, end_x: int, end_y: int, duration=0) -> None:
        driver = Application().driver
        driver.swipe(start_x, start_y, end_x, end_y, duration)

    @staticmethod
    def swipe_until_element_will_be_found_by_locator(locator: str, direction: SwipeDirection, tries=5):
        if tries > 0:
            try:
                Application().driver.find_element(AppiumBy.XPATH, locator)
                return True
            except NoSuchElementException:
                width, height = SwipeUtils.get_dimensions()

                if direction == SwipeDirection.DOWN:
                    SwipeUtils.swipe_by_coordinates(width / 2, height / 2, width / 2, height - SwipeUtils.EDGE_BORDER,
                                                    0)
                elif direction == SwipeDirection.UP:
                    SwipeUtils.swipe_by_coordinates(width / 2, height / 2, width / 2, SwipeUtils.EDGE_BORDER, 0)
                elif direction == SwipeDirection.LEFT:
                    SwipeUtils.swipe_by_coordinates(width / 2, height / 2, SwipeUtils.EDGE_BORDER, height / 2, 0)
                elif direction == SwipeDirection.RIGHT:
                    SwipeUtils.swipe_by_coordinates(width / 2, height / 2, width - SwipeUtils.EDGE_BORDER, height / 2,
                                                    0)
                return SwipeUtils.swipe_until_element_will_be_found_by_locator(locator, direction, tries - 1)
        else:
            return False

