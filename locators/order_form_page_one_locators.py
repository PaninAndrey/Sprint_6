from selenium.webdriver.common.by import By


class OrderFormPageOneLocators:
    COOKIES_BUTTON = (By.XPATH, "//button[contains(text(), 'да все привыкли')]")
    NAME_INPUT = (By.XPATH, "//input[contains(@placeholder,'* Имя')]")
    LAST_NAME_INPUT = (By.XPATH, "//input[contains(@placeholder,'* Фамилия')]")
    ADDRESS_INPUT = (By.XPATH, "//input[contains(@placeholder,'* Адрес: куда привезти заказ')]")
    STATION_INPUT = (By.XPATH, "//input[contains(@placeholder,'* Станция метро')]")
    STATION_SELECTION = (By.XPATH, "//li[@data-value='15']")
    PHONE_INPUT = (By.XPATH, "//input[contains(@placeholder,'* Телефон: на него позвонит курьер')]")
    NEXT_BUTTON = (By.XPATH, "//button[contains(text(), 'Далее')]")
