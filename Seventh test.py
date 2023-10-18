from selenium import webdriver
from selenium.webdriver.common.by import By
# Используем специальный класс Select из библиотеки WebDriver
from selenium.webdriver.support.ui import Select
import time
import math

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Ищем элементы на странице и присваиваем их значение переменным a и b
    a = browser.find_element(By.ID, "num1").text
    b = browser.find_element(By.ID, "num2").text
    # Приводим переменные a и b к типу int и считаем сумму
    sum = (int(a)+int(b))
    # Ищем элемент списка по значению select_by_value
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sum))

 # Отправляем заполненную форму
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()

finally:
    # Ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(50)
    # Закрываем браузер после всех манипуляций
    browser.quit()
