from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    """
    Класс страницы регистрации https://demoqa.ru/qa-auto/forms.
    Содержит локаторы и методы для работы с формой регистрации.
    Наследует общие методы из BasePage: click, type_text, get_text, is_visible, get_current_url.
    """

    URL = "https://demoqa.ru/qa-auto/forms"

    # Локаторы — статические (всегда одинаковые)
    FIRST_NAME = (By.XPATH, '//*[@id="firstName"]')
    LAST_NAME  = (By.XPATH, '//*[@id="lastName"]')
    EMAIL      = (By.XPATH, '//*[@id="email"]')
    PHONE      = (By.XPATH, '//*[@id="mobile"]')
    CALENDAR   = (By.XPATH, '//*[@id="dateOfBirth"]')
    ADDRESS    = (By.XPATH, '//*[@id="currentAddress"]')
    STATE      = (By.XPATH, '//*[@id="state"]')
    CITY       = (By.XPATH, '//*[@id="city"]')
    SUBMIT = (By.XPATH, '//button[@type="submit"]')
    #SUBMIT = (By.XPATH, '//button[contains(., "Отправить")]')
    #//*[@id="root"]/div/div[1]/div/div/main/div[2]/div/div/div[2]/form/button
    #//*[@id="root"]/div/div[1]/div/div/main/div[2]/div/div/div[2]/form/button/text()
    SUCCESS_MESSAGE = (By.XPATH, '//*[contains(text(), "Отправленная информация")]')

    # Локаторы — динамические (зависят от параметра)
    @staticmethod
    def gender_radio(gender: str):
        """
        Возвращает локатор радиокнопки пола.

        :param gender: 'gender-male' или 'gender-female'
        :return: tuple — локатор элемента
        """
        return By.XPATH, f'//*[@id="{gender}"]'

    @staticmethod
    def hobby_checkbox(hobby: str):
        """
        Возвращает локатор чекбокса хобби.

        :param hobby: 'hobby-sports', 'hobby-reading' или 'hobby-music'
        :return: tuple — локатор элемента
        """
        return By.XPATH, f'//*[@id="{hobby}"]'

    # Методы — действия на странице
    def open(self):
        """
        Открывает страницу регистрации.

        :return: None
        """
        super().open(self.URL)

    def fill_first_name(self, name: str):
        """
        Вводит имя в поле First Name.

        :param name: имя, например 'Alisa'
        :return: None
        """
        self.type_text(self.FIRST_NAME, name)

    def fill_last_name(self, last_name: str):
        """
        Вводит фамилию в поле Last Name.

        :param last_name: фамилия, например 'Smyth'
        :return: None
        """
        self.type_text(self.LAST_NAME, last_name)

    def fill_email(self, email: str):
        """
        Вводит email в поле Email.

        :param email: email, например 'alisa@gmail.com'
        :return: None
        """
        self.type_text(self.EMAIL, email)

    def fill_phone(self, phone: str):
        """
        Вводит номер телефона в поле Phone.

        :param phone: номер телефона, например '+78675436234'
        :return: None
        """
        self.type_text(self.PHONE, phone)

    def fill_address(self, address: str):
        """
        Вводит адрес в поле Current Address.

        :param address: адрес, например 'Moscow'
        :return: None
        """
        self.type_text(self.ADDRESS, address)

    def fill_state(self, state: str):
        """
        Вводит область в поле Область.

        :param state: область
        :return: None
        """
        self.type_text(self.STATE, state)

    def fill_city(self, city: str):
        """
        Вводит город в поле Город.

        :param city: город
        :return: None
        """
        self.type_text(self.CITY, city)

    def select_gender(self, gender: str):
        """
        Выбирает пол — кликает на радиокнопку.

        :param gender: 'gender-male' или 'gender-female'
        :return: None
        """
        self.click(self.gender_radio(gender))

    def select_hobbies(self, hobbies: list):
        """
        Выбирает хобби — кликает на каждый чекбокс из списка.

        :param hobbies: список хобби ['hobby-sports', 'hobby-reading', 'hobby-music']
        :return: None
        """
        for hobby in hobbies:
            self.click(self.hobby_checkbox(hobby))

    def submit(self):
        """
        Нажимает кнопку Submit.

        :return: None
        """
        self.click(self.SUBMIT)