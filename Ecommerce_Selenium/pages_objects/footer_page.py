from selenium.webdriver.common.by import By

class FooterPage:
    
    def __init__(self, driver):
        self.driver = driver
        
    # Loclaise le titre Subscription
    def get_titre(self):
        return self.driver.find_element(By.XPATH, "//footer//h2")
    
    # Localise la zone de saisie de l'email
    def get_email(self):
        return self.driver.find_element(By.ID, "susbscribe_email")
    
    # Rempli la zone de saisie
    def fill_form(self, table):
        self.get_email().send_keys(table[0]["email"])
        
    # Clique sur la flèche subscribe
    def click_subscribe(self):
        self.driver.find_element(By.ID, "subscribe").click()
        
    # Localise le message de validation
    def get_success(self):
        return self.driver.find_element(By.XPATH, "//div[@class='alert-success alert']")