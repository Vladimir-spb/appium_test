from element.button import Button
from element.text import Text
from page.base_page import BasePage
from page.form.apply_form import ApplyForm


class BasketPage(BasePage):
    PAGE_NAME = 'Basket Page'
    UNIQ_ELEMENT = ('//*[@resource-id="ru.dns.shop.android:id/title_text" and @text="Корзина"]', PAGE_NAME)
    EMPTY_BASKET = ('//*[@resource-id="ru.dns.shop.android:id/empty_content_summary_text"]', 'Пустая корзина')
    GO_TO_CATALOG_BUTTON = ('//*[@resource-id="ru.dns.shop.android:id/empty_content_action_button"]', 'Переход в каталог')
    NAME_ITEM = ('//*[@resource-id="ru.dns.shop.android:id/product_title_text"]', 'Название продукта')
    PRICE_ITEM = ('//*[@resource-id="ru.dns.shop.android:id/cart_item_sum_view_current_sum_text"]', 'Цена товара')
    PRICE_TOTAL = ('//*[@resource-id="ru.dns.shop.android:id/total_sum_text"]', 'Цена общая')
    DEL_ITEM = ('//*[@resource-id="ru.dns.shop.android:id/decrement_button"]', 'Удалить товар')
    DELETED_ITEM = ('//*[@resource-id="ru.dns.shop.android:id/snackbar_text"]', 'Товар удален')

    def __init__(self):
        super().__init__(*self.UNIQ_ELEMENT)
        self.__empty_basket = Text(*self.EMPTY_BASKET)
        self.__name_item = Text(*self.NAME_ITEM)
        self.__price_item = Text(*self.PRICE_ITEM)
        self.__price_total = Text(*self.PRICE_TOTAL)
        self.__deleted_item = Text(*self.DELETED_ITEM)
        self.__go_to_catalog_button = Button(*self.GO_TO_CATALOG_BUTTON)
        self.__del_item_button = Button(*self.DEL_ITEM)
        self.apply_form = ApplyForm()

    def is_basket_empty(self):
        return self.__empty_basket.check_element_on_display()

    def is_button_catalog_on_display(self):
        return self.__go_to_catalog_button.check_element_on_display()

    def get_name_item(self):
        return self.__name_item.get_text_from_element()

    def get_price_item(self):
        return self.__price_item.get_text_from_element()

    def get_price_total(self):
        return self.__price_total.get_text_from_element()

    def del_item(self):
        self.__del_item_button.click_on_element()

    def get_text_deleted_item(self):
        return self.__deleted_item.get_text_from_element()


basket_page = BasketPage()
