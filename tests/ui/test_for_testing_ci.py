import allure
from pages.demoqa_student_registration_page import RegistrationPage
from data.registration_data import STUDENT


@allure.feature("Student Registration Form")
class TestRegistrationForm:

    @allure.story("Fill and submit registration form")
    def test_fill_and_submit(self, browser) -> None:
        # Arrange
        page = RegistrationPage(browser)

        # Act
        page.open()
        page.fill_first_name(STUDENT["first_name"])
        page.fill_last_name(STUDENT["last_name"])
        page.fill_email(STUDENT["email"])
        page.select_gender(STUDENT["gender"])
        page.fill_phone(STUDENT["phone"])
        page.select_hobbies(STUDENT["hobbies"])
        page.fill_address(STUDENT["address"])
        page.fill_state(STUDENT["state"])
        page.fill_city(STUDENT["city"])
        page.submit()

        # Assert
        assert "forms" in page.get_current_url(), \
            f"Expected to stay on forms page, current URL: {page.get_current_url()}"
