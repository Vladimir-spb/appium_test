from element.button import Button
from element.text import Text
from page.base_page import BasePage
from page.form.notifications_form import NotificationsForm
from page.form.update_form import UpdateForm


class MainPage(BasePage):
    PAGE_NAME = 'Main Page'
    UNIQ_ELEMENT = ('//*[@resource-id="ru.dns.shop.android:id/logo_image"]', PAGE_NAME)
    CITY_NAME = ('//*[@resource-id="ru.dns.shop.android:id/change_current_settlement_button"]', 'Название города')
    BASKET_BUTTON = ('//*[contains(@content-desc,"Корзина")]', 'Корзина')
    PROFILE_BUTTON = ('//android.widget.FrameLayout[@content-desc="Профиль"]', 'Профиль')
    CATALOG_BUTTON = ('//android.widget.FrameLayout[@content-desc="Каталог"]', 'Каталог')


    def __init__(self):
        super().__init__(*self.UNIQ_ELEMENT)
        self.__city_name = Text(*self.CITY_NAME)
        self.__basket_button = Button(*self.BASKET_BUTTON)
        self.__profile_button = Button(*self.PROFILE_BUTTON)
        self.__catalog_button = Button(*self.CATALOG_BUTTON)
        self.notification_form = NotificationsForm()
        self.update_form = UpdateForm()

    def get_city_name_main_page(self):
        return self.__city_name.get_text_from_element()

    def click_basket(self):
        self.__basket_button.click_on_element()

    def click_profile(self):
        self.__profile_button.click_on_element()

    def click_catalog(self):
        self.__catalog_button.click_on_element()

    def get_content_from_basket_button(self):
        return self.__basket_button.find_element().get_attribute("content-desc")


main_page = MainPage()
