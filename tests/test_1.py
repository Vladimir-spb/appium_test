from page.accessories_page import accessories_page
from page.basket_page import basket_page
from page.change_city_page import change_city_page
from page.favourites_page import favourites_page
from page.form.catalog_page import catalog_page
from page.main_page import main_page
from page.meet_page import meet_page
from page.page_in import page_in
from page.profile_page import profile_page

MOSKOW_CITY = "Москва"
NEW_CITY = "Казань"


class TestAppium:

    @staticmethod
    def test_1(init_driver):
        if meet_page.uniq_element.check_element_on_display():
            name_city = meet_page.get_name_city()
            assert MOSKOW_CITY in name_city, f"На приветственной странице указан город отличный от {MOSKOW_CITY}"
            meet_page.click_change_city_button()

        assert change_city_page.uniq_element.check_element_on_display(), "Список городов не открылся"

        change_city_page.input_city_name(NEW_CITY)
        change_city_page.click_city(NEW_CITY)
        name_city = meet_page.get_name_city()
        assert NEW_CITY in name_city, f"На приветственной странице указан город отличный от {NEW_CITY}"
        meet_page.click_ok_button()

        if page_in.uniq_element.check_element_on_display():
            page_in.click_login_later()

        if main_page.notification_form.uniq_element.check_element_on_display():
            main_page.notification_form.apply_notifications()

        if main_page.update_form.uniq_element.check_element_on_display():
            main_page.update_form.close_update()

        assert main_page.uniq_element.check_element_on_display(), f"переход на страницу {main_page.PAGE_NAME} не состоялся"
        name_city = main_page.get_city_name_main_page()
        assert NEW_CITY in name_city, f"На {main_page.PAGE_NAME} странице указан город отличный от {NEW_CITY}"
        main_page.click_basket()

        assert basket_page.uniq_element.check_element_on_display(), f"переход на страницу {basket_page.PAGE_NAME} не состоялся"
        assert basket_page.is_basket_empty(), "В корзине есть товар"
        assert basket_page.is_button_catalog_on_display(), "На странице не отображается кнопка Перейти в каталог"

        main_page.click_profile()
        assert profile_page.uniq_element.check_element_on_display(), f"переход на страницу {profile_page.PAGE_NAME} не состоялся"
        assert profile_page.is_login_button_on_display(), "Кнопка Войти не отобразилась"
        name_city = profile_page.get_city_name()
        assert NEW_CITY in name_city, f"На {profile_page.PAGE_NAME} странице указан город отличный от {NEW_CITY}"

        profile_page.click_favourites_button()

        assert favourites_page.uniq_element.check_element_on_display(), f"переход на страницу {favourites_page.PAGE_NAME} не состоялся"
        assert favourites_page.is_login_button(), "Кнопка Войти в профиль не отобразилась"
        assert favourites_page.is_button_catalog_on_display(), "На странице не отображается кнопка Перейти в каталог"

    @staticmethod
    def test_2(init_driver):
        assert main_page.uniq_element.check_element_on_display(), f"переход на страницу {main_page.PAGE_NAME} не состоялся"
        main_page.click_catalog()

        assert catalog_page.uniq_element.check_element_on_display(), f"переход на страницу {catalog_page.PAGE_NAME} не состоялся"
        catalog_page.swipe_from_accessories_button()
        catalog_page.click_accessories_button()

        assert accessories_page.uniq_element.check_element_on_display(), f"переход на страницу {accessories_page.PAGE_NAME} не состоялся"
        accessories_page.click_for_mobile_button()
