from pathlib import Path

import pytest

from data.data_capa import NAME_APP
from driver.browser import Application


@pytest.fixture()
def init_driver():
    application = Application()
    application.driver.activate_app(NAME_APP)

    yield application

    application.driver.terminate_app(NAME_APP)
    application.quit()


@pytest.fixture()
def airplane_mode():
    application = Application()
    application.driver.set_network_connection(1)

    yield

    application.driver.set_network_connection(6)


@pytest.fixture()
def apk():
    application = Application()
    if not application.driver.is_app_installed("com.example.myapp"):
        application.driver.install_app(f'{Path(__file__).parent.parent}\\apk\\telegram.apk')

    yield
