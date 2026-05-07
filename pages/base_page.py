import allure
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=10)

    def open(self, url: str) -> None:
        self.driver.get(url)

    @allure.step("Click element {locator}")
    def click(self, locator: tuple) -> None:
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step("Type '{text}' into {locator}")
    def type_text(self, locator: tuple, text: str) -> None:
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: tuple) -> str:
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def is_visible(self, locator: tuple) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def get_current_url(self) -> str:
        return self.driver.current_url
