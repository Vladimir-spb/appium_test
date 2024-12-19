import logging
import time

from page.accessories_page import accessories_page
from page.basket_page import basket_page
from page.catalog_page import catalog_page
from page.change_city_page import change_city_page
from page.favourites_page import favourites_page
from page.filter_page import filter_page
from page.for_mobile_page import for_mobile_page
from page.item_page import item_page
from page.main_page import main_page
from page.meet_page import meet_page
from page.memory_card_page import memory_card_page
from page.page_in import page_in
from page.profile_page import profile_page

MOSKOW_CITY = "Москва"
NEW_CITY = "Казань"

logger = logging.getLogger("Test 1")


class TestAppium:

    @staticmethod
    def test_1(init_driver):
        # region Шаг 1: Запустить приложение
        logger.info("Шаг 1: Запустить приложение")

        if meet_page.uniq_element.check_element_on_display():
            name_city = meet_page.get_name_city()
            assert MOSKOW_CITY in name_city, f"На приветственной странице указан город отличный от {MOSKOW_CITY}"

        logger.info("Шаг 1: завершён без ошибок")
        # endregion

        # region Шаг 2: Запомнить указанный город, подтвердить выбор города
        logger.info("Шаг 2: Запомнить указанный город, подтвердить выбор города")

        meet_page.click_change_city_button()

        if change_city_page.location_form.uniq_element.check_element_on_display():
            change_city_page.location_form.cancel_location()

        change_city_page.assert_displayed_after_wait()

        change_city_page.input_city_name(NEW_CITY)
        change_city_page.click_city(NEW_CITY)
        name_city = meet_page.get_name_city()
        assert NEW_CITY in name_city, f"На приветственной странице указан город отличный от {NEW_CITY}"
        meet_page.click_ok_button()

        logger.info("Шаг 2: завершён без ошибок")
        # endregion

        # region Шаг 3:  Нажать "Войти позже"
        logger.info("Шаг 3:  Нажать 'Войти позже'")

        if page_in.uniq_element.check_element_on_display():
            page_in.click_login_later()

        logger.info("Шаг 3: завершён без ошибок")
        # endregion

        # region Шаг 4:  Разрешить отправку уведомлений"
        logger.info("Шаг 4:  Разрешить отправку уведомлений")

        if main_page.notification_form.uniq_element.check_element_on_display():
            main_page.notification_form.apply_notifications()

        if main_page.update_form.uniq_element.check_element_on_display():
            main_page.update_form.close_update()

        main_page.assert_displayed_after_wait()
        name_city = main_page.get_city_name_main_page()
        assert NEW_CITY in name_city, f"На {main_page.PAGE_NAME} странице указан город отличный от {NEW_CITY}"

        logger.info("Шаг 4: завершён без ошибок")
        # endregion

        # region Шаг 5: Запустить приложение
        logger.info("Шаг 5: Нажать на иконку с корзиной в нижнем меню")

        main_page.click_basket()
        basket_page.assert_displayed_after_wait()
        assert basket_page.is_basket_empty(), "В корзине есть товар"
        basket_page.is_button_catalog_on_display(), "На странице не отображается кнопка Перейти в каталог"

        logger.info("Шаг 5: завершён без ошибок")
        # endregion

        # region Шаг 6: Перейти в профиль (икона с человечком справа в меню навигации)
        logger.info("Шаг 6: Перейти в профиль (икона с человечком справа в меню навигации)")

        main_page.click_profile()
        profile_page.assert_displayed_after_wait()
        assert profile_page.is_login_button_on_display(), "Кнопка Войти не отобразилась"
        name_city = profile_page.get_city_name()
        assert NEW_CITY in name_city, f"На {profile_page.PAGE_NAME} странице указан город отличный от {NEW_CITY}"

        logger.info("Шаг 6: завершён без ошибок")
        # endregion

        # region Шаг 7: Нажать на кнопку "Избранное"
        logger.info("Шаг 7: Нажать на кнопку 'Избранное'")

        profile_page.click_favourites_button()
        favourites_page.assert_displayed_after_wait()
        assert favourites_page.is_login_button(), "Кнопка Войти в профиль не отобразилась"
        assert favourites_page.is_button_catalog_on_display(), "На странице не отображается кнопка Перейти в каталог"

        logger.info("Шаг 7: завершён без ошибок")
        # endregion

    @staticmethod
    def test_2(init_driver):
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

        # region Шаг 4:  Открыть фильтры
        logger.info("Шаг 4:  Открыть фильтры")

        memory_card_page.click_filter_button()
        filter_page.assert_displayed_after_wait()

        logger.info("Шаг 4: завершён без ошибок")
        # endregion

        # region Шаг 5:  В пункте "Объём ГБ" выбрать указанный в ТК объём, нажать "Применить
        logger.info("Шаг 5:  В пункте 'Объём ГБ' выбрать указанный в ТК объём, нажать 'Применить'")

        filter_page.swipe_from_size_flash_button()
        filter_page.click_size_flash_button()
        filter_page.click_size_128_gb_button()
        filter_page.click_apply_button()

        logger.info("Шаг 5: завершён без ошибок")
        # endregion

        # region Шаг 6:  Для первого товара в списке запомнить цену и название - далее цена1 и товар1
        logger.info("Шаг 6:  Для первого товара в списке запомнить цену и название - далее цена1 и товар1")

        memory_card_page.assert_displayed_after_wait()
        name = memory_card_page.get_name_item()
        price = memory_card_page.get_price()

        logger.info("Шаг 6: завершён без ошибок")
        # endregion

        # region Шаг 7:  Открыть страницу товара1
        logger.info("Шаг 7:  Открыть страницу товара1")

        memory_card_page.open_page_item()
        item_page.assert_displayed_after_wait()
        price_item = item_page.get_price()
        assert price_item == price, "Цена не совпадает"

        logger.info("Шаг 7: завершён без ошибок")
        # endregion

        # region Шаг 8:  Нажать кнопку "Купить"
        logger.info("Шаг 8:  Нажать кнопку 'Купить'")

        item_page.click_buy()

        assert item_page.get_text_buy_button() == "В корзине", "Текст на кнопке не изменился"
        assert "1" in main_page.get_content_from_basket_button(), "Цифра 1 не отобразилась рядом с иконкой корзины"

        logger.info("Шаг 8: завершён без ошибок")
        # endregion

        # region Шаг 9:  Нажать на кнопку корзины в нижнем меню
        logger.info("Шаг 9:  Нажать на кнопку корзины в нижнем меню")

        main_page.click_basket()

        basket_page.assert_displayed_after_wait()
        name_basket_item = basket_page.get_name_item()
        assert name_basket_item in name, "Имя не совпадает"
        price_item_basket = basket_page.get_price_item()
        price_total_basket = basket_page.get_price_total()
        assert price_item_basket == price, "Цена не совпадает"
        assert price_total_basket == price, "Цена не совпадает"

        logger.info("Шаг 9: завершён без ошибок")
        # endregion

        # region Шаг 10:  Удалить товар1 из корзины
        logger.info("Шаг 10:  Удалить товар1 из корзины")
        basket_page.del_item()
        basket_page.apply_form.assert_displayed_after_wait()
        basket_page.apply_form.click_delete()

        assert basket_page.is_basket_empty(), "В корзине есть товар"

        text = basket_page.get_text_deleted_item()
        assert text == "Товар удален", "Уведомление не появилось"
        logger.info("Шаг 10: завершён без ошибок")
        # endregion
