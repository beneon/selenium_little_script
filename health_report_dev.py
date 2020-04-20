import os
from selenium_setting import ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
from yaml import full_load
import numpy as np


with open('personal_info.yaml',encoding='utf8') as yaml_file:
    personal_info = full_load(yaml_file)

chrome = ChromeOptions(headless=False)

driver = chrome.get_driver()
driver.get(r'https://www.wjx.cn/m/63115031.aspx')


def select_actionchain(element,select_val:str):
    action = ActionChains(driver)
    action.move_to_element(element)
    action.click(element)
    action.key_down(Keys.DOWN)
    action.key_down(Keys.ENTER)
    action.perform()
    if element.text==select_val:
        pass
    else:
        select_actionchain(element,select_val)

ele = driver.find_element_by_id('select2-q3-container')
select_actionchain(ele,'行政后勤')

ele2 = driver.find_element_by_id('select2-q5-container')
select_actionchain(ele2,'科研科')