from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignupLoginPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
    
    # Localise le titre de la partie Signup    
    def get_titre_signup(self):
        return self.driver.find_element(By.XPATH, "//h2[text()='New User Signup!']")
    
    # Localise la zone de saisie de l'username de la partie Signup  
    def get_username(self):
        return self.driver.find_element(By.XPATH, "//input[@data-qa='signup-name']")

    # Localise la zone de saisie de l'email de la partie Signup  
    def get_email_signup(self):
        return self.driver.find_element(By.XPATH, "//input[@data-qa='signup-email']")
    
    # Rempli le formulaire pour l'inscription
    def fill_form_signup(self, table):

        self.get_username().send_keys(table[0]["username"])
        self.get_email_signup().send_keys(table[0]["email"])
    
    # Clique sur le bouton Signup
    def click_signup(self):
        self.driver.find_element(By.XPATH, "//button[text()='Signup']").click()
    
    # Localise le titre de la partie Login    
    def get_titre_login(self):
        return self.driver.find_element(By.XPATH, "//h2[text()='Login to your account']")
    
    # Localise la zone de saisie de l'email de la partie Login 
    def get_email_login(self):
        return self.driver.find_element(By.XPATH, "//input[@data-qa='login-email']")
    
    # Localise la zone de saisie du mot de passe de la partie Login 
    def get_password(self):
        return self.driver.find_element(By.XPATH, "//input[@data-qa='login-password']")
       
    # Rempli le formulaire de connexion
    def fill_form_login(self, table):

        self.get_email_login().send_keys(table[0]["email"])
        self.get_password().send_keys(table[0]["password"])
        
    # Clique sur le bouton Login
    def click_login(self):
        self.driver.find_element(By.XPATH, "//button[text()='Login']").click()
        
    # Localise le massage d'erreur en cas de mauvais login
    def get_message_erreur_login(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'incorrect')]")))
    
    # Localise le massage d'erreur en cas de compte existant
    def get_message_erreur_signup(self):
        return self.driver.find_element(By.XPATH, "//p[contains(text(), 'already exist')]")
    