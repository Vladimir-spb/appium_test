from element.button import Button
from page.base_page import BasePage


class ForMobilePage(BasePage):
    PAGE_NAME = 'For Mobile Page'
    UNIQ_ELEMENT = ('//*[@resource-id="ru.dns.shop.android:id/toolbar"]/child::*[@text="Для мобильных устройств"]', PAGE_NAME)

    CARD_OF_MEMORY_BUTTON = ('//*[@resource-id="ru.dns.shop.android:id/title_text" and @text="Карты памяти"]', 'Карты памяти')

    def __init__(self):
        super().__init__(*self.UNIQ_ELEMENT)
        self.__card_of_memory_button = Button(*self.CARD_OF_MEMORY_BUTTON)

    def click_card_of_memory_button(self):
        self.__card_of_memory_button.click_on_element()


for_mobile_page = ForMobilePage()
