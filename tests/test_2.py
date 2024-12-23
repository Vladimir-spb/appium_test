import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from driver.browser import Application
from page.accessories_page import accessories_page
from page.catalog_page import catalog_page
from page.for_mobile_page import for_mobile_page
from page.main_page import main_page
from page.memory_card_page import memory_card_page
from utils.image_utils import ImageUtils


application = Application()

logger = logging.getLogger("Test 2")


class TestAppium2:

    @staticmethod
    def test_get_screen(init_driver):
        # region Шаг 1: Запустить приложение
        logger.info("Шаг 1: Запустить приложение")

        main_page.assert_displayed_after_wait()

        logger.info("Шаг 1: завершён без ошибок")
        # endregion

        # region Шаг 2:  Нажать на иконку каталога в нижнем меню (список с лупой)
        logger.info("Шаг 2:  Нажать на иконку каталога в нижнем меню (список с лупой)")

        main_page.click_catalog()
        catalog_page.assert_displayed_after_wait()

        logger.info("Шаг 2: завершён без ошибок")
        # endregion

        # region Шаг 3:  Перейти в меню "Аксессуары и услуги > Для мобильных устройств > Карты памяти"
        logger.info("Шаг 3:  Перейти в меню 'Аксессуары и услуги > Для мобильных устройств > Карты памяти'")

        catalog_page.swipe_from_accessories_button()
        catalog_page.click_accessories_button()
        accessories_page.assert_displayed_after_wait()
        accessories_page.click_for_mobile_button()
        for_mobile_page.assert_displayed_after_wait()
        for_mobile_page.click_card_of_memory_button()
        memory_card_page.assert_displayed_after_wait()

        logger.info("Шаг 3: завершён без ошибок")
        # endregion

        # region Шаг 4:  Проверить что кнопка купить оранжевого цвета"
        logger.info("Шаг 4:  Проверить что кнопка купить оранжевого цвета")

        path = memory_card_page.get_screenshot_buy_button()
        color_orange = ImageUtils.get_color_image(path)
        assert color_orange == [253, 140, 11], "Цвет кнопки не оранжевый"

        logger.info("Шаг 4: завершён без ошибок")
        # endregion

    @staticmethod
    def test_wifi(init_driver, airplane_mode):
        # region Шаг 1: Запустить приложение
        logger.info("Шаг 1: Запустить приложение")

        main_page.assert_displayed_after_wait()

        logger.info("Шаг 1: завершён без ошибок")
        # endregion

        # region Шаг 2: Кликнуть на корзину
        logger.info("Шаг 2: Кликнуть на корзину")
        main_page.click_basket()
        logger.info("Шаг 2: завершён без ошибок")
        # endregion

        # region Шаг 3: Отобразилась ошибка об отсутствии интернета
        logger.info("Шаг 3: Отобразилась ошибка об отсутствии интернета")
        main_page.error_text_is_displayed()
        logger.info("Шаг 3: завершён без ошибок")
        # endregion

    @staticmethod
    def test_change_app(init_driver, apk):
        # region Шаг 1: Запустить приложение
        logger.info("Шаг 1: Запустить приложение")

        main_page.assert_displayed_after_wait()

        logger.info("Шаг 1: завершён без ошибок")
        # endregion

        # region Шаг 2: Сменить приложение
        logger.info("Шаг 2: Сменить приложение")
        application.driver.activate_app("org.telegram.messenger")

        locator = "//*[@text='Telegram']"
        element = WebDriverWait(application.driver, 30).until(EC.presence_of_element_located((By.XPATH, locator)))
        assert element.is_displayed(), "Приложение не переключилось"

        logger.info("Шаг 2: завершён без ошибок")
        # endregion
