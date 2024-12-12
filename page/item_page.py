from element.button import Button
from element.text import Text
from page.base_page import BasePage


class ItemPage(BasePage):
    PAGE_NAME = 'Item Page'
    UNIQ_ELEMENT = ('//*[@resource-id="ru.dns.shop.android:id/product_title_text"]', PAGE_NAME)

    BUY_ITEM = ('//*[@resource-id="ru.dns.shop.android:id/buy_button"]', 'Купить')
    PRICE_ITEM = ('//*[@resource-id="ru.dns.shop.android:id/current_price_text"]', 'Цена продукта')

    def __init__(self):
        super().__init__(*self.UNIQ_ELEMENT)
        self.__price_item = Text(*self.PRICE_ITEM)
        self.__buy_button = Button(*self.BUY_ITEM)

    def get_price(self):
        return self.__price_item.get_text_from_element()

    def click_buy(self):
        self.__buy_button.click_on_element()

    def get_text_buy_button(self):
        return self.__buy_button.get_text_from_element()


item_page = ItemPage()
