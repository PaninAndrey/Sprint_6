from selenium.webdriver.common.by import By


class MainPageLocators:
    UPPER_ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    LOWER_ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    KEY_QUESTIONS_SECTION = (By.CLASS_NAME, "accordion")

    @staticmethod
    def header(number):
        return By.ID, f'accordion__heading-{number}'

    @staticmethod
    def header_answer(number):
        return By.XPATH, f'//div[@id="accordion__panel-{number}"]//p'