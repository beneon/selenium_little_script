from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class ChromeOptions:
    options = Options()

    options.binary_location = r"C:\Program Files (x86)\Google\Chrome Beta\Application\chrome.exe"

    def __init__(self,headless=True):
        if headless:
            self.options.add_argument('--headless')

    def get_driver(self):
        driver = webdriver.Chrome(r"C:\chromedriver_win32\chromedriver.exe",options=self.options)
        return driver