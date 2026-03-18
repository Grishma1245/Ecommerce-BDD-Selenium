from behave import given, when, then
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

@given('I have added the "{product_name}" to my cart')
@when('I add the "{product_name}" to my cart')
def step_impl(context, product_name):
    context.inventory_page.add_product_to_cart(product_name)

@then('the cart badge should show "{count}" item')
@then('the cart badge should show "{count}" items')
def step_impl(context, count):
    try:
        actual_count = context.inventory_page.get_cart_item_count()
        assert actual_count == count
    except AssertionError as e:
        print(f"DEBUG: Expected badge {count}, got {actual_count}")
        raise e

@then('the cart badge should be empty')
def step_impl(context):
    import time
    time.sleep(1)
    try:
        actual_count = context.inventory_page.get_cart_item_count()
        assert actual_count == "0"
    except AssertionError as e:
        print(f"DEBUG: Expected empty badge, got {actual_count}")
        raise e

@given('I am on the cart page')
@when('I go to the cart page')
def step_impl(context):
    context.inventory_page.go_to_cart()
    context.cart_page = CartPage(context.driver)

@then('the cart page should display the "{product_name}"')
def step_impl(context, product_name):
    if not hasattr(context, 'cart_page'):
        context.inventory_page.go_to_cart()
        context.cart_page = CartPage(context.driver)
    try:
        assert context.cart_page.is_item_in_cart(product_name)
    except AssertionError as e:
        print(f"DEBUG: Cart page source: {context.driver.page_source[:500]}...")
        raise e

@then('the cart page should not display the "{product_name}"')
def step_impl(context, product_name):
    if not hasattr(context, 'cart_page'):
        context.inventory_page.go_to_cart()
        context.cart_page = CartPage(context.driver)
    try:
        assert not context.cart_page.is_item_in_cart(product_name)
    except AssertionError as e:
        print(f"DEBUG: Item {product_name} still found in cart")
        raise e

@given('I am on the cart page with "{product_name}"')
def step_impl(context, product_name):
    context.inventory_page.add_product_to_cart(product_name)
    context.inventory_page.go_to_cart()
    context.cart_page = CartPage(context.driver)

@when('I remove the "{product_name}" from the cart')
def step_impl(context, product_name):
    if not hasattr(context, 'cart_page'):
        context.inventory_page.go_to_cart()
        context.cart_page = CartPage(context.driver)
    context.cart_page.remove_item(product_name)
