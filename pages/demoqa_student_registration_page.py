import os

import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RegistrationPage(BasePage):

    URL = os.environ["REGISTRATION_PAGE_URL"]

    FIRST_NAME      = (By.XPATH, '//*[@id="firstName"]')
    LAST_NAME       = (By.XPATH, '//*[@id="lastName"]')
    EMAIL           = (By.XPATH, '//*[@id="email"]')
    PHONE           = (By.XPATH, '//*[@id="mobile"]')
    CALENDAR        = (By.XPATH, '//*[@id="dateOfBirth"]')
    ADDRESS         = (By.XPATH, '//*[@id="currentAddress"]')
    STATE           = (By.XPATH, '//*[@id="state"]')
    CITY            = (By.XPATH, '//*[@id="city"]')
    SUBMIT          = (By.XPATH, '//button[@type="submit"]')
    SUCCESS_MESSAGE = (By.XPATH, '//*[contains(text(), "Отправленная информация")]')

    @staticmethod
    def gender_radio(gender: str) -> tuple:
        return By.XPATH, f'//*[@id="{gender}"]'

    @staticmethod
    def hobby_checkbox(hobby: str) -> tuple:
        return By.XPATH, f'//*[@id="{hobby}"]'

    @allure.step("Open registration page")
    def open(self) -> None:
        super().open(self.URL)

    @allure.step("Fill first name: {name}")
    def fill_first_name(self, name: str) -> None:
        self.type_text(self.FIRST_NAME, name)

    @allure.step("Fill last name: {last_name}")
    def fill_last_name(self, last_name: str) -> None:
        self.type_text(self.LAST_NAME, last_name)

    @allure.step("Fill email: {email}")
    def fill_email(self, email: str) -> None:
        self.type_text(self.EMAIL, email)

    @allure.step("Fill phone: {phone}")
    def fill_phone(self, phone: str) -> None:
        self.type_text(self.PHONE, phone)

    @allure.step("Fill address: {address}")
    def fill_address(self, address: str) -> None:
        self.type_text(self.ADDRESS, address)

    @allure.step("Fill state: {state}")
    def fill_state(self, state: str) -> None:
        self.type_text(self.STATE, state)

    @allure.step("Fill city: {city}")
    def fill_city(self, city: str) -> None:
        self.type_text(self.CITY, city)

    @allure.step("Select gender: {gender}")
    def select_gender(self, gender: str) -> None:
        self.click(self.gender_radio(gender))

    @allure.step("Select hobbies: {hobbies}")
    def select_hobbies(self, hobbies: list) -> None:
        for hobby in hobbies:
            self.click(self.hobby_checkbox(hobby))

    @allure.step("Submit form")
    def submit(self) -> None:
        self.click(self.SUBMIT)
