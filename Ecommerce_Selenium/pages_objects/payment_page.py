from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PaymentPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 2)
        
    # Localise le nom de la carte
    def get_name(self):
        return self.driver.find_element(By.NAME, "name_on_card")
    
    # Localise le numéro de la carte
    def get_number(self):
        return self.driver.find_element(By.NAME, "card_number")
    
    # Localise le CVC
    def get_cvc(self):
        return self.driver.find_element(By.NAME, "cvc")
    
    # Localise le mois d'expiration
    def get_expiry_mounth(self):
        return self.driver.find_element(By.NAME, "expiry_month")
    
    # Localise l'année d'expiration
    def get_expiry_year(self):
        return self.driver.find_element(By.NAME, "expiry_year")
    
     # Remplie le formulaire
    def fill_form(self, table):
        self.get_name().send_keys(table[0]["name"])
        self.get_number().send_keys(table[0]["number"])
        self.get_cvc().send_keys(table[0]["cvc"])
        self.get_expiry_mounth().send_keys(table[0]["expiry mounth"])
        self.get_expiry_year().send_keys(table[0]["expiry year"])
        
    # Clique sur Pay and Confirm Order   
    def click_pay(self):
        self.driver.find_element(By.ID, "submit").click()
       
    # Localise le message de validation
    def get_success(self):
        try:
            return self.wait.until(EC.presence_of_element_located((By.ID, "success_message"))).text
        except:
            return None
    