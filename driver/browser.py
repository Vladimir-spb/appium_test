from appium import webdriver

from driver.singleton import Singleton


class Application(metaclass=Singleton):
    def __init__(self, url_app, capabil):
        self.__appium_driver = webdriver.Remote(url_app, options=capabil)

    def quit(self):
        self.__appium_driver.quit()
