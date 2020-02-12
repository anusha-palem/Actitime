from selenium.webdriver import Chrome
driver=Chrome('E:\chromedriver.exe')
driver.maximize_window()
driver.get('https://demo.actitime.com/login.do')