import math
import time

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    browser.execute_script("window.scrollBy(0, 100);")  # JavaScript
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    input2 = browser.find_element_by_id("robotCheckbox")
    input2.click()
    input3 = browser.find_element_by_id("robotsRule")
    input3.click()
    button = browser.find_element_by_tag_name("button")
    button.click()
    assert True
finally:
    time.sleep(10)
    browser.quit()
