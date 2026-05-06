import os                        # стандартная библиотека Python для работы с системой
import pytest                    # фреймворк для тестов — нужен чтобы использовать @pytest.fixture
from selenium import webdriver   # библиотека для управления браузером


@pytest.fixture                  # говорим pytest что это фикстура — она будет запускаться перед каждым тестом
def browser():                   # название фикстуры — именно это имя ты пишешь в аргументах теста
    """
    Открывает браузер Chrome перед каждым тестом.
    Закрывает браузер после каждого теста.
    :return: экземпляр браузера WebDriver
    """

    options = webdriver.ChromeOptions()   # создаём объект с настройками браузера

    options.add_argument("--incognito")           # режим инкогнито — без сохранения истории и кук
    options.add_argument("--disable-autofill")    # отключить автозаполнение форм

    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,       # отключить сохранение паролей
        "profile.password_manager_enabled": False, # отключить менеджер паролей
        "autofill.profile_enabled": False,         # отключить автозаполнение профиля
        "autofill.address_enabled": False          # отключить автозаполнение адреса
    })

    # os.getenv("CI") проверяет есть ли переменная окружения CI
    # GitHub Actions автоматически выставляет CI=true на каждом запуске
    # локально эта переменная не задана — значит блок не выполнится
    if os.getenv("CI"):
        options.add_argument("--headless")              # без окна — на сервере нет экрана
        options.add_argument("--no-sandbox")            # нужно для запуска Chrome на Linux
        options.add_argument("--disable-dev-shm-usage") # нужно для стабильной работы Chrome на Linux

    driver = webdriver.Chrome(options=options)   # создаём браузер с нашими настройками
    driver.maximize_window()                     # разворачиваем окно на весь экран

    yield driver        # передаём браузер в тест — тест выполняется здесь

    driver.quit()       # после теста закрываем браузер — выполняется всегда, даже если тест упал