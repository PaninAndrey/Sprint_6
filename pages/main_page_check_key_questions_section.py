import allure
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


class CheckKeyQuestionsSection(MainPage):

    @allure.step("Скролл до блока 'Вопросы о важном'")
    def scroll_to_question_section(self):
        self.scroll_to_element(MainPageLocators.KEY_QUESTIONS_SECTION)

    @allure.step("Клик на заголовке с вопросом")
    def click_on_header(self, header_number):
        element = MainPageLocators.header(header_number)
        self.click_on_element(element)

    @allure.step("Получить текст ответа на вопрос")
    def get_text_answer(self, header_number):
        element = MainPageLocators.header_answer(header_number)
        return self.get_text_on_element(element)
