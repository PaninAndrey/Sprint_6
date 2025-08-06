import allure
from pages.main_page import MainPage
from locators.order_form_page_two_locators import OrderFormPageTwoLocators


class OrderFormPageTwo(MainPage):

    @allure.step("Заполнить форму заказа первым набором данных на второй странице"
                 " оформления заказа")
    def fill_up_order_form_page_two_with_first_set_of_data(self, comment):
        self.click_on_element(OrderFormPageTwoLocators.DATE_INPUT_FIELD)
        self.click_on_element(OrderFormPageTwoLocators.DATE_INPUT_14_MAY)
        self.click_on_element(OrderFormPageTwoLocators.RENTAL_PERIOD_FIELD)
        self.click_on_element(OrderFormPageTwoLocators.RENTAL_PERIOD_INPUT_3_DAYS)
        self.click_on_element(OrderFormPageTwoLocators.SCOOTER_COLOR_INPUT_GREY)
        self.send_keys_to_input(OrderFormPageTwoLocators.COMMENT_FOR_COURIER_INPUT, comment)

    @allure.step("Заполнить форму заказа вторым набором данных на второй странице"
                 " оформления заказа")
    def fill_up_order_form_page_two_with_second_set_of_data(self, comment):
        self.click_on_element(OrderFormPageTwoLocators.DATE_INPUT_FIELD)
        self.click_on_element(OrderFormPageTwoLocators.DATE_INPUT_9_MAY)
        self.click_on_element(OrderFormPageTwoLocators.RENTAL_PERIOD_FIELD)
        self.click_on_element(OrderFormPageTwoLocators.RENTAL_PERIOD_INPUT_5_DAYS)
        self.click_on_element(OrderFormPageTwoLocators.SCOOTER_COLOR_INPUT_BLACK)
        self.send_keys_to_input(OrderFormPageTwoLocators.COMMENT_FOR_COURIER_INPUT, comment)

    @allure.step("Нажать на кнопку 'Заказать' на второй странице"
                 " оформления заказа")
    def press_order_button(self):
        element = OrderFormPageTwoLocators.ORDER_BUTTON
        self.click_on_element(element)

    @allure.step("Нажать на кнопку 'Да' на странице"
                 " подтверждения оформления заказа")
    def press_yes_button(self):
        element = OrderFormPageTwoLocators.YES_BUTTON
        self.click_on_element(element)

    @allure.step("Получить текст с кнопки 'Посмотреть статус'"
                 " в окне после оформления заказа")
    def get_text_confirmation(self):
        element = OrderFormPageTwoLocators.ORDER_CONFIRMATION_WINDOW
        return self.get_text_on_element(element)