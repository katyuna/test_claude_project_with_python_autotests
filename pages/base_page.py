from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:

    def __init__(self, driver):
        """
        Сохраняем браузер и настраиваем ожидание максимум 10 секунд.

        :param driver:
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=10)

    def open(self, url):
        """
        Открывает страницу по адресу url.

        :param url:
        :return: None
        """
        self.driver.get(url)

    def click(self, locator):
        """
        Кликает по элементу. Сначала ждёт до 10 секунд пока элемент станет кликабельным — потом кликает.
        Если элемент не появился за 10 сек, тест упадёт с ошибкой TimeoutException.

        :param locator:
        :return: None
        """
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type_text(self, locator, text):
       """
       Ждёт пока поле появится на странице, затем очищает его (на случай если там уже что-то есть)
       и вводит нужный текст.

       :param locator:
       :param text:
       :return:
       """
       element = self.wait.until(EC.visibility_of_element_located(locator))
       element.clear()
       element.send_keys(text)

    def get_text(self, locator):
        """
        Возвращает текст элемента.

        :param locator: локатор элемента
        :return: str
        """
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def is_visible(self, locator):
        """
         Проверяет виден ли элемент на странице.

        :param locator:
        :return: bool
        """
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def get_current_url(self):
        """
        Возвращает текущий URL страницы в браузере.

        :return: str
        """
        return self.driver.current_url
