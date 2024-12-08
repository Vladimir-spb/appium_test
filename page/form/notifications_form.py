from element.button import Button
from page.base_page import BasePage


class NotificationsForm(BasePage):
    PAGE_NAME = 'Notifications Form'
    UNIQ_ELEMENT = ('//*[@resource-id="com.android.permissioncontroller:id/permission_message"]', PAGE_NAME)
    APPlY_BUTTON = ('//*[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]', 'Кнопка "Разрешить"')

    def __init__(self):
        super().__init__(*self.UNIQ_ELEMENT)
        self.__apply_button = Button(*self.APPlY_BUTTON)

    def apply_notifications(self):
        self.__apply_button.click_on_element()
