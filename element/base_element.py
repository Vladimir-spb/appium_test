import logging
from abc import ABC

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from driver.browser import Application

logger = logging.getLogger("Base Element")

application = Application()


class BaseElementClass(ABC):

    def __init__(self, loc, name_of):
        self._locator = loc
        self._name = name_of

    def get_locator(self):
        return self._locator

    def get_name(self):
        return self._name

    def find_element(self):
        try:
            wait = WebDriverWait(application.driver, 30)
            element = wait.until(EC.presence_of_element_located((By.XPATH, self.get_locator())))
            logger.info(f'выполняется поиск элемента {self.get_name()} на странице')
            return element
        except Exception as e:
            logger.error(f'все рухнуло при попытке найти элемент {self.get_name()} на странице, '
                         f'подробности смотри {e}')

    def find_elements(self):
        try:
            wait = WebDriverWait(application.driver, 30)
            elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, self.get_locator())))
            logger.info(f'выполняется поиск элемента {self.get_name()} на странице')
            return elements
        except Exception as e:
            logger.error(f'все рухнуло когда пытались получить элементы {self.get_name()}, '
                         f'подробности смотри {e}')

    def click_on_element(self):
        try:
            self.find_element().click()
            logger.info(f'выполняется клик по элементу {self.get_name()}')
        except Exception as e:
            logger.error(f'все рухнуло при попытке клика по элементу {self.get_name()}, '
                         f'подробности смотри {e}')

    def check_element_on_display(self):
        try:
            element = self.find_element()
            logger.info(f'выполнена проверка на наличие элемента {self.get_name()} на странице')
            return element.is_displayed()
        except Exception as e:
            logger.error(f'проверка на наличие элемента {self.get_name()} на странице не прошла, '
                         f'подробности смотри {e}')

    def get_text_from_element(self):
        try:
            element = self.find_element()
            logger.info(f'получаем текст из элемента {self.get_name()}')
            return element.text
        except Exception as e:
            logger.error(f'все рухнуло когда пытались получить текст из элемента {self.get_name()}, '
                         f'подробности смотри {e}')

    def send_keys(self, value):
        self.find_element().send_keys(value)
