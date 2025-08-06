import pytest
import allure
from pages.main_page_check_key_questions_section import CheckKeyQuestionsSection
import data


class TestKeyQuestionsSection:
    @allure.title("Тесты на соответствие текста в выпадающем окне в разделе 'Вопросы о важном'")
    @pytest.mark.parametrize('header_number, expected_text', data.KeyQuestionsAnswers.answers)
    def test_correct_answers_text(self, driver, header_number, expected_text):
        check_answer = CheckKeyQuestionsSection(driver)
        check_answer.scroll_to_question_section()
        check_answer.click_on_header(header_number)
        key_answer_text = check_answer.get_text_answer(header_number)
        assert key_answer_text == expected_text

