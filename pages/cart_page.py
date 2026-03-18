from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class CartPage(BasePage):
    # Locators
    TITLE = (By.CLASS_NAME, "title")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        super().__init__(driver)

    def is_on_page(self):
        return self.is_visible(self.TITLE) and self.get_text(self.TITLE) == "Your Cart"

    def get_cart_items(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located(self.CART_ITEMS)
            )
        except:
            pass
        return self.find_elements(self.CART_ITEMS) if self.is_visible(self.CART_ITEMS) else []

    def is_item_in_cart(self, item_name):
        items = self.get_cart_items()
        item_names = []
        for item in items:
            name_element = item.find_element(By.CLASS_NAME, "inventory_item_name")
            name = name_element.text.strip()
            item_names.append(name)
            if name.lower() == item_name.strip().lower():
                return True
        if items:
            print(f"DEBUG: Items in cart: {item_names}")
        return False

    def add_item(self, item_name):
        """Adds an item to the cart from the products page"""
        # Wait until product is visible
        product_locator = (By.XPATH, f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button")
        button = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(product_locator)
        )
        button.click()

    def remove_item(self, item_name):
        """Removes an item from the cart page"""
        items = self.get_cart_items()
        for item in items:
            name_element = item.find_element(By.CLASS_NAME, "inventory_item_name")
            if name_element.text.strip().lower() == item_name.strip().lower():
                # Wait until Remove button is clickable
                remove_button = WebDriverWait(item, 5).until(
                    EC.element_to_be_clickable((By.TAG_NAME, "button"))
                )
                remove_button.click()
                return
        raise Exception(f"Item '{item_name}' not found in cart to remove")

    def get_cart_count(self):
        """Returns the number of items in the cart badge"""
        try:
            badge = WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located(self.CART_BADGE)
            )
            return int(badge.text.strip())
        except:
            return 0

    def click_checkout(self):
        """Clicks the checkout button on cart page"""
        button = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        )
        button.click()