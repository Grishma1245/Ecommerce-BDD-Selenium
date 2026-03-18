from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
# from behave.api import StepNotImplementedError
# # from behave.api.pending_step import StepNotImplementedError


@given('I open the login page')
def step_open_login(context):
    # Setup driver
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service)
    context.driver.maximize_window()
    
    # Open URL
    context.driver.get("https://www.saucedemo.com/")
    
    # Initialize LoginPage object
    context.login_page = LoginPage(context.driver)

# @given('I open the login page')
# def step_open_login(context):
#     service = Service(ChromeDriverManager().install())
#     context.driver = webdriver.Chrome(service=service)
#     context.driver.maximize_window()
#     context.driver.get("https://www.saucedemo.com/")

# @when('I am on the login page')
# def step_impl(context):
#     context.login_page = LoginPage(context.driver)
#     context.login_page.open()

@when('I enter valid username and password')
def step_impl(context):
    context.login_page.login("standard_user", "secret_sauce")

@when('I enter invalid username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.login_page.login(username, password)

@when('I click the login button')
def step_impl(context):
    # The login method already clicks but for explicit step:
    # context.login_page.click(context.login_page.LOGIN_BUTTON)
    pass

@then('I should be redirected to the products page')
def step_impl(context):
    context.inventory_page = InventoryPage(context.driver)
    assert context.inventory_page.is_on_page()

@then('I should see an error message')
def step_impl(context):
    assert context.login_page.is_visible(context.login_page.ERROR_MESSAGE)

@given('I am logged in as a standard user')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open()
    context.login_page.login("standard_user", "secret_sauce")
    context.inventory_page = InventoryPage(context.driver)
    assert context.inventory_page.is_on_page(), "Login was not successful"

# @given(u'I am on the login page')
# def step_impl(context):
#     raise StepNotImplementedError(u'Given I am on the login page')



