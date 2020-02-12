import unittest
import json
from lib.utils import create_driver
from lib.ui. acti_login import LoginPage
from lib.ui.acti_homepage import HomePage
from selenium.webdriver.common.keys import Keys

class test_login(unittest.TestCase):
    def setUp(self):
        self.driver=create_driver.get_driver_instance()
        self.login= LoginPage(self.driver)
        self.home= HomePage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_login_page(self):
        data=json.load(open('./test/regression/login/data.json'))
        self.login.wait_for_login_page_to_load()
        self.login.get_username_textbox().send_keys(data['TC_01']['username'])
        self.login.get_password_textbox().send_keys(data['TC_01']['pwd'],Keys.ENTER)
        self.home.wait_home_page_to_load()
        actual_title=self.driver.title
        expected_title=data['TC_01']['title']
        assert actual_title==expected_title, "Title not matching"
        self.home.get_logout_button().click()
        self.login.wait_for_login_page_to_load()
        actual_title = self.driver.title
        expected_title = 'actiTIME - Login'
        assert actual_title == expected_title, "Title not matching"



