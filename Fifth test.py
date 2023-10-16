from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
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
    # Отмечаем checkbox "I'm the robot"
    input2 = browser.find_element(By.ID, "robotCheckbox")
    input2.click()
    # Выбираем radiobutton "Robots rule!".
    input3 = browser.find_element(By.CSS_SELECTOR, "[value= 'robots']")
    input3.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(50)
    # закрываем браузер после всех манипуляций
    browser.quit()