from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class SignupFormPage:
    
    def __init__(self, driver):
        self.driver = driver
      
    # Localise le titre de la page  
    def get_titre(self):
        return self.driver.find_element(By.XPATH, "//b[text()='Enter Account Information']")
    
    # Localise la zone de saisie du mot de passe du formulaire
    def get_password(self):
        return self.driver.find_element(By.ID, "password")
    
    # Localise la zone de saisie du prénom du formulaire
    def get_first_name(self):
        return self.driver.find_element(By.ID, "first_name")

    # Localise la zone de saisie du nom du formulaire
    def get_last_name(self):
        return self.driver.find_element(By.ID, "last_name")

    # Localise la zone de saisie de l'adresse
    def get_address1(self):
        return self.driver.find_element(By.ID, "address1")

    # Localise la zone de saisie de la région
    def get_state(self):
        return self.driver.find_element(By.ID, "state")

    # Localise la zone de saisie de la ville
    def get_city(self):
        return self.driver.find_element(By.ID, "city")
    
    # Localise la zone de saisie du code postal
    def get_zipcode(self):
        return self.driver.find_element(By.ID, "zipcode")
    
    # Localise la zone de saisie du téléphone
    def get_phone(self):
        return self.driver.find_element(By.ID, "mobile_number")

    # Localise la liste déroulante du pays
    def get_country(self):
        return Select(self.driver.find_element(By.ID, "country"))
    
    # Localise la liste déroulante du jour
    def get_day_anniversary(self):
        return Select(self.driver.find_element(By.ID, "days"))
    
    # Localise la liste déroulante du mois
    def get_month_anniversary(self):
        return Select(self.driver.find_element(By.ID, "months"))
    
    # Localise la liste déroulante de l'année
    def get_year_anniversary(self):
        return Select(self.driver.find_element(By.ID, "years"))
    
    # Localise le bouton radio du genre masculin
    def get_radio_gender(self):
        return self.driver.find_element(By.ID, "uniform-id_gender1")
    
    # Rempli le formulaire d'inscription avec les informations personnelles du client
    def fill_form(self, table):

        # Rempli les textbox
        self.get_password().send_keys(table[0]["password"])
        self.get_first_name().send_keys(table[0]["firstname"])
        self.get_last_name().send_keys(table[0]["lastname"])
        self.get_address1().send_keys(table[0]["address"])
        self.get_state().send_keys(table[0]["state"])
        self.get_city().send_keys(table[0]["city"])
        self.get_zipcode().send_keys(table[0]["zipcode"])
        self.get_phone().send_keys(table[0]["phone"])

        # Rempli les select box
        self.get_country().select_by_visible_text(table[0]["country"])
        self.get_day_anniversary().select_by_visible_text(table[0]["jourAnniversaire"])
        self.get_month_anniversary().select_by_visible_text(table[0]["moisAnniversaire"])
        self.get_year_anniversary().select_by_visible_text(table[0]["anneeAnniversaire"])
        
        # Bouton radio
        self.get_radio_gender().click()
        
        # Checkbox
        self.click_checkbox_signup()
        self.click_checkbox_receive()
    
    # Clique sur le checkbox signup  
    def click_checkbox_signup(self):
         radio_element = self.driver.find_element(By.XPATH, "//label[@for='newsletter']")

         # 2. Vérifier si elle n'est PAS déjà sélectionnée (.is_selected() vérifie l'état 'coché')
         if not radio_element.is_selected():
             # 3. Si elle n'est pas cochée, alors on clique pour la cocher
             return radio_element.click()
         return None
    
    # Clique sur le checkbox receive  
    def click_checkbox_receive(self):
         radio_element = self.driver.find_element(By.XPATH, "//label[@for='optin']")

         # 2. Vérifier si elle n'est PAS déjà sélectionnée (.is_selected() vérifie l'état 'coché')
         if not radio_element.is_selected():
             # 3. Si elle n'est pas cochée, alors on clique pour la cocher
             return radio_element.click()
         return None
    
    # Clique sur le bouton Create
    def click_create(self):
        self.driver.find_element(By.XPATH, "//button[text()='Create Account']").click()