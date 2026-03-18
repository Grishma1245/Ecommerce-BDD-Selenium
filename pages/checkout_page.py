from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    # Info Step Locators
    TITLE = (By.CLASS_NAME, "title")
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    
    # Overview Step Locators
    FINISH_BUTTON = (By.ID, "finish")
    
    # Complete Step Locators
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        super().__init__(driver)

    def is_on_info_page(self):
        return self.is_visible(self.TITLE) and self.get_text(self.TITLE) == "Checkout: Your Information"

    def enter_shipping_info(self, first_name="John", last_name="Doe", zip_code="12345"):
        self.enter_text(self.FIRST_NAME_INPUT, first_name)
        self.enter_text(self.LAST_NAME_INPUT, last_name)
        self.enter_text(self.POSTAL_CODE_INPUT, zip_code)

    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)

    def is_on_overview_page(self):
        return self.is_visible(self.TITLE) and self.get_text(self.TITLE) == "Checkout: Overview"

    def click_finish(self):
        self.click(self.FINISH_BUTTON)

    def is_on_complete_page(self):
        return self.is_visible(self.TITLE) and self.get_text(self.TITLE) == "Checkout: Complete!"

    def get_success_message(self):
        return self.get_text(self.COMPLETE_HEADER)
