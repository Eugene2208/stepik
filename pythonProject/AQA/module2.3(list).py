import math
import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text
    x = str(int(num1) + int(num2))
    print (x)
    # browser.find_element_by_tag_name("select").click()
    # browser.find_element_by_css_selector("option:nth-child(2)").click()
    # 2nd option
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(x)  # ищем элемент с текстом "Python"

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    # не забываем оставить пустую строку в конце файла
