from selenium.webdriver.common.by import By

class CheckoutPage:
    
    def __init__(self, driver):
        self.driver = driver
        
    # Localise le nom complet de l'adresse de livraison
    def get_name_delivery(self):
        return self.driver.find_element(By.XPATH, "//ul[@id='address_delivery']/li[@class='address_firstname address_lastname' and normalize-space()]")

    # Localise l'adresse de l'adresse de livraison
    def get_address_delivery(self):
        return self.driver.find_element(By.XPATH, "//ul[@id='address_delivery']/li[@class='address_address1 address_address2' and normalize-space()]")

    # Localise la ville avec son code postal de l'adresse de livraison
    def get_city_delivery(self):
        return self.driver.find_element(By.XPATH, "//ul[@id='address_delivery']/li[@class='address_city address_state_name address_postcode' and normalize-space()]")
    
    # Localise le pays de l'adresse de livraison
    def get_country_delivery(self):
        return self.driver.find_element(By.XPATH, "//ul[@id='address_delivery']/li[@class='address_country_name']")
    
    # Localise le téléphone de l'adresse de livraison
    def get_phone_delivery(self):
        return self.driver.find_element(By.XPATH, "//ul[@id='address_delivery']/li[@class='address_phone']")
    
    # Localise la zone de saisie description
    def get_description(self):
        return self.driver.find_element(By.TAG_NAME, "textarea")
    
    # Remplie la zone description
    def fill_description(self, table):
        self.get_description().send_keys(table[0]["description"])
        
    # Clique sur Place order   
    def click_order(self):
        self.driver.find_element(By.XPATH, "//a[@href='/payment']").click()
        
     # Localise le nom complet de l'adresse de paiement
    def get_name_bill(self):
        return self.driver.find_element(By.XPATH, "//ul[@id='address_invoice']/li[@class='address_firstname address_lastname' and normalize-space()]")

    # Localise l'adresse de l'adresse de paiement
    def get_address_bill(self):
        return self.driver.find_element(By.XPATH, "//ul[@id='address_invoice']/li[@class='address_address1 address_address2' and normalize-space()]")

    # Localise la ville avec son code postal de l'adresse de paiement
    def get_city_bill(self):
        return self.driver.find_element(By.XPATH, "//ul[@id='address_invoice']/li[@class='address_city address_state_name address_postcode' and normalize-space()]")
    
    # Localise le pays de l'adresse de paiement
    def get_country_bill(self):
        return self.driver.find_element(By.XPATH, "//ul[@id='address_invoice']/li[@class='address_country_name']")
    
    # Localise le téléphone de l'adresse de paiement
    def get_phone_bill(self):
        return self.driver.find_element(By.XPATH, "//ul[@id='address_invoice']/li[@class='address_phone']")