from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'https://SunInJuly.github.io/execute_script.html'

def calc(x):
    return str(math.log(abs(12*math.sin(x))))
    
try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = int(browser.find_element(By.ID, 'input_value').text)
    result_func = calc(x)
    answer_field = browser.find_element(By.ID, 'answer')
    answer_field.send_keys(result_func)
    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()
    radiobutton = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()
    submitbutton = browser.find_element(By.CLASS_NAME, 'btn')
    submitbutton.click()
    

finally:
    time.sleep(15)
    browser.quit()