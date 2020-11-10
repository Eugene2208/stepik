import math
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")

    )
    button = browser.find_element_by_css_selector("#book")
    button.click()
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    browser.find_element_by_id("solve").click()
    #message = browser.find_element_by_id("verify_message")
finally:
    time.sleep(10)
    browser.quit()
