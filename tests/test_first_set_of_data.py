import allure


from pages.order_form_page_one import OrderFormPageOne
from data import FirstSetOfData
from data import FirstCommentForCourier
from pages.order_form_page_two import OrderFormPageTwo
from tests.conftest import driver
from pages.transitions import Transitions
from curl import *


class TestOrderWithFirstSetOfData:
    @allure.title("Заполнение формы заказа"
                  " самоката с первым набором данных")
    def test_order_form_with_first_set_of_data(self, driver):
        name = FirstSetOfData.name
        last_name = FirstSetOfData.last_name
        address = FirstSetOfData.address
        phone = FirstSetOfData.phone
        first_order_page_one = OrderFormPageOne(driver)
        first_order_page_one.press_main_page_upper_order_button()
        first_order_page_one.press_cookies_button()
        first_order_page_one.fill_up_order_form_page_one(name, last_name, address, phone)
        first_order_page_one.press_next_button()
        first_order_page_two = OrderFormPageTwo(driver)
        comment = FirstCommentForCourier.comment_for_first_set_of_data
        first_order_page_two.fill_up_order_form_page_two_with_first_set_of_data(comment)
        first_order_page_two.press_order_button()
        first_order_page_two.press_yes_button()
        order_confirmation = first_order_page_two.get_text_confirmation()
        assert order_confirmation == "Посмотреть статус"

    @allure.title("Проверка перехода со страницы оформления заказа"
                  " самоката на главную страницу сервиса")
    def test_transition_from_order_page_to_main_page(self, driver):
        scooter_confirmation = TestOrderWithFirstSetOfData()
        scooter_confirmation.test_order_form_with_first_set_of_data(driver)
        scooter_transition = Transitions(driver)
        scooter_transition.press_confirmation_button()
        scooter_transition.press_scooter_button()
        assert driver.current_url == main_site

    @allure.title("Проверка перехода со страницы оформления заказа"
                  " самоката на главную страницу Я.Дзен")
    def test_transition_from_order_page_to_dzen_page(self, driver):
        scooter_confirmation = TestOrderWithFirstSetOfData()
        scooter_confirmation.test_order_form_with_first_set_of_data(driver)
        dzen_transition = Transitions(driver)
        dzen_transition.press_confirmation_button()
        dzen_transition.press_dzen_button()
        assert dzen_transition.switch_and_get_url(expected_url) == expected_url

