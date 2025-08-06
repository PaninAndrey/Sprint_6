from selenium.webdriver.common.by import By


class TransitionLocators:
    STATUS_BUTTON = (By.XPATH, "//button[contains(text(), 'Посмотреть статус')]")
    SCOOTER_TRANSITION_BUTTON = (By.XPATH, "//img[@alt='Scooter']")
    DZEN_TRANSITION_BUTTON = (By.XPATH, "//img[@alt='Yandex']")
