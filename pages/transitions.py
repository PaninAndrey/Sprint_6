import allure

from pages.main_page import MainPage
from locators.transition_locators import TransitionLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    @allure.step("Получение url со страницы Дзен")
    def switch_and_get_url(self, expected_url, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.number_of_windows_to_be(2))
            self.driver.switch_to.window(self.driver.window_handles[-1])
            WebDriverWait(self.driver, timeout).until(EC.url_to_be(expected_url))
            return self.driver.current_url
        except:
            return None