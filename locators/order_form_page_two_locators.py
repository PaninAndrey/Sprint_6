from selenium.webdriver.common.by import By


class OrderFormPageTwoLocators:
    DATE_INPUT_FIELD = (By.XPATH, "//input[contains(@placeholder,'* Когда привезти самокат')]")
    DATE_INPUT_14_MAY = (By.XPATH, "//div[contains(@aria-label,'Choose среда, 14-е мая 2025 г.')]")
    DATE_INPUT_9_MAY = (By.XPATH, "//div[contains(@aria-label,'Choose пятница, 9-е мая 2025 г.')]")
    RENTAL_PERIOD_FIELD = (By.XPATH, "//div[contains(text(), '* Срок аренды')]")
    RENTAL_PERIOD_INPUT_3_DAYS = (By.XPATH, "//div[contains(text(), 'трое суток')]")
    RENTAL_PERIOD_INPUT_5_DAYS = (By.XPATH, "//div[contains(text(), 'пятеро суток')]")
    SCOOTER_COLOR_INPUT_GREY = (By.ID, "grey")
    SCOOTER_COLOR_INPUT_BLACK = (By.ID, "black")
    COMMENT_FOR_COURIER_INPUT = (By.XPATH, "//input[contains(@placeholder,'Комментарий для курьера')]")
    ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    YES_BUTTON = (By.XPATH, "//button[contains(text(), 'Да')]")
    ORDER_CONFIRMATION_WINDOW = (By.XPATH, "//button[contains(text(), 'Посмотреть статус')]")