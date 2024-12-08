from element.button import Button
from page.base_page import BasePage


class LocationForm(BasePage):
    PAGE_NAME = 'Location Form'
    UNIQ_ELEMENT = ('//*[contains(@text,"местоположении устройства")]', PAGE_NAME)
    CANCEL_BUTTON = ('//*[@resource-id="com.android.permissioncontroller:id/permission_deny_button"]', 'Кнопка "Запретить"')

    def __init__(self):
        super().__init__(*self.UNIQ_ELEMENT)
        self.__cancel_button = Button(*self.CANCEL_BUTTON)

    def cancel_location(self):
        self.__cancel_button.click_on_element()
