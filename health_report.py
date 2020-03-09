import os
from selenium_setting import ChromeOptions
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


def text_question_fill(question_id,text2input):
    question_ele = driver.find_element_by_id(question_id)
    question_ele.clear()
    question_ele.send_keys(text2input)

text_question_fill('q1',personal_info['name'])
text_question_fill('q2',personal_info['fosu_id'])

selector_q3 = Select(driver.find_element_by_id('q3'))
selector_q3.select_by_value('7')

q4 = driver.find_element_by_id('q4')
q4.click()
time.sleep(1)

#frame switch
driver.switch_to.frame(driver.find_element_by_id('div__calendarIframe'))
#click today
driver.find_element_by_id('selectTodayButton').click()
driver.switch_to.default_content()


selector_q5 = Select(driver.find_element_by_id('q5'))
selector_q5.select_by_value('9')

temperature_decimal = np.random.randint(2,6,2)
text_question_fill('q6',f"36.{temperature_decimal[0]}")
text_question_fill('q7',f"36.{temperature_decimal[1]}")


def click_one_div(question_div_id:str, click_index:int, content_should_be='无', ui_class='ui-checkbox', jq_class='jqcheck'):
    check_boxes = driver.find_element_by_id(question_div_id).find_elements_by_class_name(ui_class)
    click_one = check_boxes[click_index]
    print(click_one.find_element_by_class_name('label'))
    assert click_one.find_element_by_class_name('label').text == content_should_be, f"提供的click_index：{click_index}不正确"
    click_one.find_element_by_class_name(jq_class).click()


click_one_div('div8', -1)
click_one_div('div9', -1)
click_one_div('div10', 0, content_should_be='回院上班', ui_class='ui-radio', jq_class='jqradio')
click_one_div('div11', 0)

text_question_fill('q12','无')

