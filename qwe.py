from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from driver.browser import Application
from page.form.catalog_page import catalog_page
from page.meet_page import meet_page

application = Application()

catalog_page.swipe_from_accessories_button()
