from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    # открываем страницу
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # нажимаем на кнопку
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()
    # принимаем confirm
    confirm = browser.switch_to.alert
    confirm.accept()
    # решаем выражение
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    # Считаем значение для переменной x
    x_element = browser.find_element(By.ID, "input_value")
    # Получаем текстовое значение этого элемента
    x = x_element.text
    print(x)
    input1 = browser.find_element(By.ID, "answer")
    # Подставляем значение x в функцию calc()
    y = calc(x)
    print(y)
    input1.send_keys(y)
    # отправляем заполненную форму
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()

finally:
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

