from selenium.webdriver.common.by import By

class ContactPage:
    
    def __init__(self, driver):
        self.driver = driver
    
    def get_titre_form(self):
        return self.driver.find_element(By.XPATH, "//h2[text()='Get In Touch']")
    
    # Localise la zone de saisie du name
    def get_name(self):
        return self.driver.find_element(By.XPATH, "//input[@data-qa='name']")
    
    # Localise la zone de saisie du mail
    def get_email(self):
        return self.driver.find_element(By.XPATH, "//input[@data-qa='email']")
    
    # Localise la zone de saisie du sujet
    def get_subject(self):
        return self.driver.find_element(By.XPATH, "//input[@data-qa='subject']")
    
    # Localise la zone de saisie du message
    def get_message(self):
        return self.driver.find_element(By.ID, "message")
    
    # Rempli le formulaire
    def fill_form(self, table):

        self.get_name().send_keys(table[0]["name"])
        self.get_email().send_keys(table[0]["email"])
        self.get_subject().send_keys(table[0]["subject"])
        self.get_message().send_keys(table[0]["message"])
    
    # Upload le fichier
    def upload_file(self):

        self.driver.find_element(By.XPATH,"//input[@type='file']").send_keys("C:/Projet/Ecommerce_Selenium/fichier/Photo.bmp")
    
    # Clique sur le bouton Submit
    def click_submit(self):
        self.driver.find_element(By.XPATH, "//input[@name='submit']").click()
        
    # Accepte la pop up de confirmation
    def accept_alert(self):
        # Attendre l'apparition de l'alerte
        alerte = self.driver.switch_to.alert

        # Clique sur OK
        alerte.accept()
        
    # Localise le message de succès de l'envoi du message
    def get_success(self):
        return self.driver.find_element(By.XPATH, "//div[@class='status alert alert-success']")
    
    # Clique sur le bouton home
    def click_home(self):
        self.driver.find_element(By.XPATH, "//a[@href='/']").click()