from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class ChromeOptions:
    options = Options()

    options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

    def __init__(self,headless=True):
        self.options.add_argument('--no-sandbox')
        if headless:
            self.options.add_argument('--headless')

    def get_driver(self):
        driver = webdriver.Chrome(r"C:\chromedriver\chromedriver.exe",options=self.options)
        return driver