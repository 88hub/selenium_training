from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    num = int(browser.find_element(By.ID, 'input_value').text)
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(calc(num))

    button1 = browser.find_element(By.TAG_NAME, 'button')
    button1.click()

finally:
    time.sleep(5)
    browser.quit()