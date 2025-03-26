import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

'''
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))
print(file_path)
'''

link = 'http://suninjuly.github.io/file_input.html'
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

try:
    browser = webdriver.Chrome()
    browser.get(link)
    first_name = browser.find_element(By.NAME, 'firstname')
    first_name.send_keys('A')
    last_name = browser.find_element(By.NAME, 'lastname')
    last_name.send_keys('S')
    email = browser.find_element(By.NAME, 'email')
    email.send_keys('as@sa.su')
    add_file_button = browser.find_element(By.ID, 'file')
    add_file_button.send_keys(file_path)
    submit_button = browser.find_element(By.CLASS_NAME, 'btn')
    submit_button.click()
    
finally:
    time.sleep(15)
    browser.quit()


