from appium import webdriver

from data.data_capa import CAPABIL
from driver.singleton import Singleton
from settings.capabilities import Capabilities
from settings.settings import Settings


class Application(Singleton):
    def __init__(self):
        self.__appium_driver = webdriver.Remote(Settings.URL_APPIUM, options=Capabilities.get_capabil(CAPABIL))

    @property
    def driver(self) -> webdriver:
        return self.__appium_driver

    def quit(self):
        self.driver.quit()
