import math
import time

from selenium import webdriver
    # alert = browser.switch_to.alert  # всплывающее окно с кнопкой подтверждения
    # alert_text = alert.text  # получить текст
    # alert.accept()  # принять alert
    #
    # confirm = browser.switch_to.alert  # alert с доп. кнопкой отказа
    # confirm.accept()  # принять confirm
    # confirm.dismiss()  # метод для отказа
    #
    # prompt = browser.switch_to.alert  # confirm с доп. полем для текста
    # prompt.send_keys("My answer")
    # prompt.accept()
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)
    button = browser.find_element_by_tag_name("button")
    button.click()
    alert = browser.switch_to.alert  # всплывающее окно с кнопкой подтверждения
    alert_text = alert.text  # получить текст
    alert.accept()  # принять alert
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    button.click()
finally:
    time.sleep(10)
    browser.quit()
