from element.button import Button
from page.base_page import BasePage


class AccessoriesPage(BasePage):
    PAGE_NAME = 'Accessories Page'
    UNIQ_ELEMENT = ('//*[@text="Аксессуары и услуги"]', PAGE_NAME)

    FOR_MOBILE_BUTTON = ('//*[@resource-id="ru.dns.shop.android:id/title_text" and @text="Для мобильных устройств"]', 'Для мобильных устройств')

    def __init__(self):
        super().__init__(*self.UNIQ_ELEMENT)
        self.__for_mobile_button = Button(*self.FOR_MOBILE_BUTTON)

    def click_for_mobile_button(self):
        self.__for_mobile_button.click_on_element()


accessories_page = AccessoriesPage()
