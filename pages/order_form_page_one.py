import allure

from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from locators.order_form_page_one_locators import OrderFormPageOneLocators


class OrderFormPageOne(MainPage):

    @allure.step("Нажать на кнопку заказа в верхнем правом углу главной страницы")
    def press_main_page_upper_order_button(self):
        element = MainPageLocators.UPPER_ORDER_BUTTON
        self.click_on_element(element)

    @allure.step("Нажать на кнопку заказа в нижней части главной страницы"
                 " после раздела 'Как это работает'")
    def press_main_page_lower_order_button(self):
        element = MainPageLocators.LOWER_ORDER_BUTTON
        self.scroll_to_element(element)
        self.click_on_element(element)

    @allure.step("Нажать на кнопку согласия на использования файлов cookie")
    def press_cookies_button(self):
        element = OrderFormPageOneLocators.COOKIES_BUTTON
        self.click_on_element(element)

    @allure.step("Заполнить форму заказа на первой странице"
                 "оформления заказа")
    def fill_up_order_form_page_one(self, name, last_name, address, phone):
        self.send_keys_to_input(OrderFormPageOneLocators.NAME_INPUT, name)
        self.send_keys_to_input(OrderFormPageOneLocators.LAST_NAME_INPUT, last_name)
        self.send_keys_to_input(OrderFormPageOneLocators.ADDRESS_INPUT, address)
        self.click_on_element(OrderFormPageOneLocators.STATION_INPUT)
        self.click_on_element(OrderFormPageOneLocators.STATION_SELECTION)
        self.send_keys_to_input(OrderFormPageOneLocators.PHONE_INPUT, phone)

    @allure.step("Нажать на кнопку 'Далее' на первой странице оформления заказа")
    def press_next_button(self):
        element = OrderFormPageOneLocators.NEXT_BUTTON
        self.click_on_element(element)