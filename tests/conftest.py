import pytest
from data.data_capa import CAPABIL
from driver.browser import Application
from settings.capabilities import Capabilities
from settings.settings import Settings


@pytest.fixture()
def init_driver():
    Application(Settings.URL_APPIUM, Capabilities.get_capabil(CAPABIL))

    yield

    Application().quit()
