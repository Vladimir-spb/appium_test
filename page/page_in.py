from element.button import Button
from page.base_page import BasePage


class PageIn(BasePage):
    PAGE_NAME = 'Page In'
    UNIQ_ELEMENT = ('//*[@resource-id="ru.dns.shop.android:id/login_button"]', PAGE_NAME)
    LOGIN_LATER = ('//*[@resource-id="ru.dns.shop.android:id/skip_auth_button"]', 'Кнопка войти позже')

    def __init__(self):
        super().__init__(*self.UNIQ_ELEMENT)
        self.__login_later_button = Button(*self.LOGIN_LATER)

    def click_login_later(self):
        self.__login_later_button.click_on_element()


page_in = PageIn()
