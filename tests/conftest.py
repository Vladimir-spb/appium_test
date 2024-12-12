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
