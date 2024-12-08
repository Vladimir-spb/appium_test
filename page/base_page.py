import logging

from element.uniq_element import UniqElement

logger = logging.getLogger("Base Element")


class BasePage:
    def __init__(self, locator, screen_name):
        self.locator = locator
        self.screen_name = screen_name

    def wait_for_displayed(self) -> bool:
        logger.info(f"Checking is screen {self.screen_name} displayed")
        return self.uniq_element.check_element_on_display()

    def assert_displayed_after_wait(self):
        assert self.wait_for_displayed(), f"{self.screen_name} is not displayed"
        logger.info(f"Screen {self.screen_name} is displayed")

    @property
    def uniq_element(self):
        return UniqElement(self.locator, self.screen_name)
