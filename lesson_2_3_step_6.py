from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element(By.TAG_NAME, 'button')
    button1.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    num = int(browser.find_element(By.ID, 'input_value').text)

    form = browser.find_element(By.ID, 'answer')
    form.send_keys(calc(num))

    button2 = browser.find_element(By.TAG_NAME, 'button')
    button2.click()

finally:
    time.sleep(5)
    browser.quit()