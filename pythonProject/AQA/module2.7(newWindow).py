import math
import time

from selenium import webdriver

# browser.switch_to.window(window_name)  # переход на новую вкладку
# new_window = browser.window_handles[1]  # получаем вкладку по ее номеру
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    button = browser.find_element_by_tag_name("button")
    button.click()
    browser.switch_to.window(browser.window_handles[1])  # переход на новую вкладку
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    browser.find_element_by_css_selector("button").click()
finally:
    time.sleep(10)
    browser.quit()
