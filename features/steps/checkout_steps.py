from behave import given, when, then
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@given('I am on the checkout information page')
def step_impl(context):
    if not hasattr(context, 'cart_page'):
        context.inventory_page.go_to_cart()
        context.cart_page = CartPage(context.driver)
    context.cart_page.click_checkout()
    context.checkout_page = CheckoutPage(context.driver)
    assert context.checkout_page.is_on_info_page()

@when('I fill in my personal information')
def step_impl(context):
    context.checkout_page.enter_shipping_info("Test", "User", "12345")

@when('I continue to the checkout overview')
def step_impl(context):
    context.checkout_page.click_continue()
    assert context.checkout_page.is_on_overview_page()

@when('I finish the checkout')
def step_impl(context):
    context.checkout_page.click_finish()

@then('I should see a success message "{expected_msg}"')
def step_impl(context, expected_msg):
    assert context.checkout_page.is_on_complete_page()
    assert expected_msg in context.checkout_page.get_success_message()
