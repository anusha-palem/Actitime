from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class HomePage:
    def __init__(self,driver):
        self.driver= driver

    def wait_home_page_to_load(self):
        wait= WebDriverWait(self.driver,30)
        wait.until(expected_conditions.visibility_of(self.get_logout_button()))

    def get_logout_button(self):
        try:
            return self.driver.find_element_by_link_text('Logout')
        except:
            return None


