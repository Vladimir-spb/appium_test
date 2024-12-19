from element.button import Button
from element.text import Text
from page.base_page import BasePage


class FavouritesPage(BasePage):
    PAGE_NAME = 'Favourites Page'
    UNIQ_ELEMENT = ('//*[@text="Избранное"]', PAGE_NAME)

    LOGIN_BUTTON = ('//*[@resource-id="ru.dns.shop.android:id/login_button"]', 'Войти в профиль')
    GO_TO_CATALOG_BUTTON = ('//*[@resource-id="ru.dns.shop.android:id/empty_content_action_button"]', 'Переход в каталог')

    def __init__(self):
        super().__init__(*self.UNIQ_ELEMENT)
        self.__login_button = Button(*self.LOGIN_BUTTON)
        self.__go_to_catalog_button = Button(*self.GO_TO_CATALOG_BUTTON)

    def is_login_button(self):
        return self.__login_button.check_element_on_display()

    def is_button_catalog_on_display(self):
        return self.__go_to_catalog_button.check_element_on_display()


favourites_page = FavouritesPage()
