import os
from selenium_setting import ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
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


def text_question_fill(question_id,text2input):
    question_ele = driver.find_element_by_id(question_id)
    question_ele.clear()
    question_ele.send_keys(text2input)

text_question_fill('q1',personal_info['name'])
text_question_fill('q2',personal_info['fosu_id'])

# 问卷星现在不用select对象了
# selector_q3 = Select(driver.find_element_by_id('q3'))
# selector_q3.select_by_value('7')

ele = driver.find_element_by_id('select2-q3-container')
select_actionchain(ele,'行政后勤')


q4 = driver.find_element_by_id('q4')
q4.click()
time.sleep(0.2)

#frame switch
driver.switch_to.frame(driver.find_element_by_id('div__calendarIframe'))
#click today
driver.find_element_by_id('selectTodayButton').click()
driver.switch_to.default_content()

# 同理，不过这里有一个录入框，说不定可以通过send_keys解决
# 不过search box没有id……所以还是继续按两次下然后再说吧
# selector_q5 = Select(driver.find_element_by_id('q5'))
# selector_q5.select_by_value('9')
ele2 = driver.find_element_by_id('select2-q5-container')
select_actionchain(ele2,'科研科')

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

