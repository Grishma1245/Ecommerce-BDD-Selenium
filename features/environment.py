from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

def before_all(context):
    pass

def before_scenario(context, scenario):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--headless")
    
    context.driver = webdriver.Chrome(options=options)
    context.driver.implicitly_wait(10)

def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.quit()
