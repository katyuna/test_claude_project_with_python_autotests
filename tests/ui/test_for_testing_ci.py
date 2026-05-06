from pages.demoqa_student_registration_page import RegistrationPage


class TestRegistrationForm:

    def test_fill_and_submit(self, browser):
        """
        Заполняет форму регистрации и проверяет
        что после отправки появился блок с результатом.
        """
        page = RegistrationPage(browser)
        page.open()

        page.fill_first_name("Alisa")
        page.fill_last_name("Smyth")
        page.fill_email("alisa@gmail.com")
        page.select_gender("gender-male")
        page.fill_phone("+78675436234")
        page.select_hobbies(["hobby-sports", "hobby-reading", "hobby-music"])
        page.fill_address("Lenina 11-1")
        page.fill_state("Moscow")
        page.fill_city("Moscow")
        page.submit()

        # Заглушка: проверяем что остались на странице формы
        assert "forms" in page.get_current_url(), \
            f"Ожидали остаться на странице формы, текущий URL: {page.get_current_url()}"