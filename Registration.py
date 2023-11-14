import unittest
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class RegistrationTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.link = "http://suninjuly.github.io/registration1.html"

# тест в стиле unittest для страницы: http://suninjuly.github.io/registration1.html
    def test_registration1(self):
        self.browser.get(self.link)
        input1 = self.browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
        input1.send_keys("Ivan")
        input2 = self.browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
        input2.send_keys("Petrov")
        input3 = self.browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
        input3.send_keys("petrov@mail.ru")
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        # финальная проверка в тесте в стиле unittest используя метод assertEqual
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    # тест в стиле unittest для страницы: http://suninjuly.github.io/registration2.html
    def test_registration2(self):
        self.link = "http://suninjuly.github.io/registration2.html"
        self.browser.get(self.link)
        input1 = self.browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
        input1.send_keys("Ivan")
        input2 = self.browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
        input2.send_keys("Petrov")
        input3 = self.browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
        input3.send_keys("petrov@mail.ru")
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        # финальная проверка в тесте в стиле unittest используя метод assertEqual
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def tearDown(self):
        self.browser.quit()
# if __name__ == "__main__" служит для подтверждения того, что данный скрипт был запущен напрямую, а не вызван внутри другого файла в качестве модуля
if __name__ == "__main__":
    unittest.main()
