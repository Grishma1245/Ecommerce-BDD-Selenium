from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    # Locators
    TITLE = (By.CLASS_NAME, "title")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    
    def __init__(self, driver):
        super().__init__(driver)

    def is_on_page(self):
        return self.is_visible(self.TITLE) and self.get_text(self.TITLE) == "Products"

    def get_product_add_button_locator(self, product_name):
        # sauce labs backpack -> add-to-cart-sauce-labs-backpack
        formatted_name = product_name.lower().replace(" ", "-")
        return (By.ID, f"add-to-cart-{formatted_name}")

    def get_product_remove_button_locator(self, product_name):
        formatted_name = product_name.lower().replace(" ", "-")
        return (By.ID, f"remove-{formatted_name}")

    def add_product_to_cart(self, product_name):
        items = self.find_elements(self.INVENTORY_ITEMS)
        for item in items:
            name_element = item.find_element(By.CLASS_NAME, "inventory_item_name")
            if name_element.text.strip() == product_name.strip():
                buttons = item.find_elements(By.TAG_NAME, "button")
                for btn in buttons:
                    if "add to cart" in btn.text.lower():
                        btn.click()
                        return
        raise Exception(f"Product '{product_name}' not found")

    def remove_product_from_cart(self, product_name):
        self.click(self.get_product_remove_button_locator(product_name))

    def get_cart_item_count(self):
        if self.is_visible(self.CART_BADGE):
            return self.get_text(self.CART_BADGE)
        return "0"

    def go_to_cart(self):
        self.click(self.CART_LINK)
        import time
        time.sleep(1)
