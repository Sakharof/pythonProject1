from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
# Открываем страницу http://suninjuly.github.io/explicit_wait2.html
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
# Задаем кнопку
    button = browser.find_element(By.ID, "book")
# Дожидаемся, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
# Нажимаем на кнопку "Book"
    button.click()
# Команда, которая проскроллит страницу на 150 пикселей вниз:
    browser.execute_script("window.scrollBy(0, 150);")
# Решить математическую задачу
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
# Отправляем заполненную форму
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()
finally:
# Ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
# Закрываем браузер после всех манипуляций
    browser.quit()