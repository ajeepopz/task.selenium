
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class LoginAutomation:
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def boot(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.sleep(5)

    def sleep(self,second):
        sleep(second)

    def inputBox(self,value,keys):
        self.driver.find_element(by=By.NAME,value=value).send_keys(keys)
        self.sleep(5)

    def quit(self):
        self.driver.quit()

    def login(self):
        self.boot()
        self.inputBox('user-name', self.username)
        self.inputBox('password', self.password)

    def getTitle(self):
        return self.driver.title

    def getURL(self):
        return self.driver.current_url

    def sourceCode(self):
        return self.driver.page_source



url = 'https://www.saucedemo.com/'
obj = LoginAutomation(url, 'standard_user', 'secret_sauce')
obj.login()
print(obj.getURL())
print(obj.getTitle())
print(obj.sourceCode())
obj.quit()
