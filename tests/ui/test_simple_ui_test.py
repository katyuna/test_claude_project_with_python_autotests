from selenium import webdriver
from selenium.webdriver.ie.service import Service
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Это плохой тест чисто для примера
def main():
    print("Инициализация браузера")

    options = webdriver.ChromeOptions()

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    input_name_locator = (By.XPATH, '//*[@id = "firstName"]')
    input_lastname_locator = (By.XPATH, '//*[@id="lastName"]')
    input_email_locator = (By.XPATH, '//*[@id="email"]')
    radio_button_gender = lambda gender: (By.XPATH, f'// *[ @ id = "{gender}"]')
    input_phone_number_locator = (By.XPATH, '//*[@id="mobile"]')
    input_calendar = (By.XPATH, '//*[@id="dateOfBirth"]')
    select_date = (By.XPATH, '//*[@id="radix-_r_j_"]/div/div[3]/button[3]')
    check_box_hobbies_locator = lambda hobby: (By.XPATH, f'//*[@id="{hobby}"]')
    text_area_locator = (By.XPATH, '//*[@id="currentAddress"]')
    input_area_locator = (By.XPATH, '//*[@id="state"]')
    input_city_locator = (By.XPATH, '//*[@id="city"]')
    submit_button_locator = (By.XPATH, '//*[@id="submitButton"]')

    hobbies = ["hobby-sports", "hobby-reading", "hobby-music"]

    def set_hobbies(driver: WebDriver, hobbies: list[str]):
        for hobby in hobbies:
            driver.find_element(*check_box_hobbies_locator(hobby=hobby)).click()

    wait = WebDriverWait(driver, timeout=10)

    try:
        driver.get("https://demoqa.ru/qa-auto/forms")

        wait.until(EC.visibility_of_element_located(input_name_locator)).send_keys("Alisa")
        driver.find_element(*input_lastname_locator).send_keys("Smyth")
        driver.find_element(*input_email_locator).send_keys("alisa@gmail.com")
        driver.find_element(*radio_button_gender(gender='gender-male')).click()
        driver.find_element(*input_phone_number_locator).send_keys("+78675436234")
        driver.find_element(*input_calendar).click()
        driver.find_element(*select_date).click()
        driver.find_element(*input_calendar).send_keys(Keys.ENTER)
        set_hobbies(driver=driver, hobbies=hobbies)
        driver.find_element(*text_area_locator).send_keys("some text")
        driver.find_element(*input_area_locator).send_keys("Moscow")
        driver.find_element(*input_city_locator).send_keys("Moscow")

    except Exception as e:
        print(f"Произошла ошибка {e}")
    finally:
        driver.quit()
        print("Браузер закрыт")


if __name__ == "__main__":
    main()
