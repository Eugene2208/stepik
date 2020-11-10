import os
import time

from selenium import webdriver

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    browser.find_element_by_name("firstname").send_keys("firstname")
    browser.find_element_by_name("lastname").send_keys("lastname")
    browser.find_element_by_name("email").send_keys("email@gmail.com")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, '../file.txt')           # добавляем к этому пути имя файла
    element =browser.find_element_by_id("file")
    element.send_keys(file_path)
    button = browser.find_element_by_tag_name("button")
    button.click()
    assert True
finally:
    time.sleep(10)
    browser.quit()