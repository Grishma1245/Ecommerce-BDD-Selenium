from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

def before_all(context):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # Commented out headless mode to show real browser flow
    # options.add_argument("--headless")
    
    # Disable password saving and 'data breach' popups
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
        "profile.default_content_setting_values.notifications": 2,
        "safebrowsing.enabled": False
    }
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    
    # Explicitly disable Password Leak Detection and other popups
    options.add_argument("--disable-features=PasswordLeakDetection,SafeBrowsing")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-save-password-bubble")
    
    context.driver = webdriver.Chrome(options=options)
    context.driver.implicitly_wait(10)

def before_scenario(context, scenario):
    if hasattr(context, 'driver'):
        # Navigate to domain to ensure we can clear its storage
        context.driver.get("https://www.saucedemo.com/")
        context.driver.delete_all_cookies()
        try:
            context.driver.execute_script("window.localStorage.clear();")
            context.driver.execute_script("window.sessionStorage.clear();")
            # Force a reload to ensure clean state is applied
            context.driver.refresh()
        except:
            pass

def after_scenario(context, scenario):
    pass

def after_all(context):
    if hasattr(context, 'driver'):
        context.driver.quit()
