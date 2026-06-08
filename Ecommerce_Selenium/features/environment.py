import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from pages_objects.account_created_page import AccountCreatedPage
from pages_objects.cart_page import CartPage
from pages_objects.checkout_page import CheckoutPage
from pages_objects.contact_page import ContactPage
from pages_objects.delete_account_page import DeletedAccountPage
from pages_objects.footer_page import FooterPage
from pages_objects.home_page import HomePage
from pages_objects.list_products_page import ListProductsPage
from pages_objects.menu_page import MenuPage
from pages_objects.order_placed_page import OrderPlacedPage
from pages_objects.payment_page import PaymentPage
from pages_objects.product_detail_page import ProductDetailPage
from pages_objects.search_product_page import SearchProductPage
from pages_objects.signup_login_page import SignupLoginPage
from pages_objects.signup_form_page import SignupFormPage


def before_scenario(context, scenario):
    download_dir = os.path.join(os.getcwd(), "downloads")
        
    chrome_options = Options()

    # 1. Désactive le gestionnaire de mots de passe et téléchargment
    prefs = {
        "download.default_directory": download_dir,
                  
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
        }
    chrome_options.add_experimental_option("prefs", prefs)

    # 2. Désactive les infobulles et notifications
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-save-password-bubble")
    chrome_options.add_argument("--safebrowsing-disable-download-protection")
    chrome_options.add_argument("--safebrowsing-disable-extension-blacklist")
    
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    
    context.driver = driver
    driver.get("https://automationexercise.com/")
    click_autoriser(driver)
    
    context.home = HomePage(driver)
    context.menu = MenuPage(driver)
    context.signup_login = SignupLoginPage(driver)
    context.signup = SignupFormPage(driver)
    context.account_created = AccountCreatedPage(driver)
    context.deleted_account = DeletedAccountPage(driver)
    context.contact = ContactPage(driver)
    context.list_products = ListProductsPage(driver)
    context.product_detail = ProductDetailPage(driver)
    context.search_product = SearchProductPage(driver)
    context.footer = FooterPage(driver)
    context.cart = CartPage(driver)
    context.checkout = CheckoutPage(driver)
    context.payment = PaymentPage(driver)
    context.order_placed = OrderPlacedPage(driver)
  
def after_scenario(context, scenario):
    time.sleep(2)
    context.driver.quit()

# Clique pour autoriser le consentement des données   
def click_autoriser(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button//p[text()='Autoriser']"))).click()