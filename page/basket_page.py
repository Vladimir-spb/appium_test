from element.button import Button
from element.text import Text
from page.base_page import BasePage
from page.form.location_form import LocationForm


class BasketPage(BasePage):
    PAGE_NAME = 'Basket Page'
    UNIQ_ELEMENT = ('//*[@resource-id="ru.dns.shop.android:id/title_text" and @text="Корзина"]', PAGE_NAME)
    EMPTY_BASKET = ('//*[@resource-id="ru.dns.shop.android:id/empty_content_summary_text"]', 'Пустая корзина')
    GO_TO_CATALOG_BUTTON = ('//*[@resource-id="ru.dns.shop.android:id/empty_content_action_button"]', 'Переход в каталог')

    def __init__(self):
        super().__init__(*self.UNIQ_ELEMENT)
        self.__empty_basket = Text(*self.EMPTY_BASKET)
        self.__go_to_catalog_button = Button(*self.GO_TO_CATALOG_BUTTON)

    def is_basket_empty(self):
        return self.__empty_basket.check_element_on_display()

    def is_button_catalog_on_display(self):
        return self.__go_to_catalog_button.check_element_on_display()


basket_page = BasketPage()
