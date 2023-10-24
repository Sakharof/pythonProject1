from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    # открывает страницу
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # нажатие на кнопку
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()
    # используем метод window_handles, который возвращает массив имён всех вкладок, чтобы узнать имя новой вкладки
    new_window = browser.window_handles[1]
    # переключение на новую вкладку
    browser.switch_to.window(new_window)
    # решение выражения
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    # считаем значение для переменной x
    x_element = browser.find_element(By.ID, "input_value")
    # получаем текстовое значение этого элемента
    x = x_element.text
    print(x)
    input1 = browser.find_element(By.ID, "answer")
    # подставляем значение x в функцию calc()
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

