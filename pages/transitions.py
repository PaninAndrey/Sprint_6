import allure

from pages.main_page import MainPage
from locators.transition_locators import TransitionLocators


class Transitions(MainPage):
    @allure.step("Нажать на кнопку 'Посмотреть статус'")
    def press_confirmation_button(self):
        element = TransitionLocators.STATUS_BUTTON
        self.click_on_element(element)

    @allure.step("Нажать на иконку 'Самокат' для перехода на главную страницу")
    def press_scooter_button(self):
        element = TransitionLocators.SCOOTER_TRANSITION_BUTTON
        self.click_on_element(element)

    @allure.step("Нажать на иконку 'Яндекс' для перехода на страницу 'Дзен'")
    def press_dzen_button(self):
        element = TransitionLocators.DZEN_TRANSITION_BUTTON
        self.click_on_element(element)
