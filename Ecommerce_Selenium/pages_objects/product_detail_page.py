from selenium.webdriver.common.by import By

class ProductDetailPage:
    
    def __init__(self, driver):
        self.driver = driver

    # Localise le nom
    def get_name(self):
        return self.driver.find_element(By.XPATH, "//div[@class='product-information']/h2[normalize-space()]")
    
    # Localise la catégorie
    def get_category(self):
         # Récupére tout le texte
        full_text = self.driver.find_element(By.XPATH, "//div[@class='product-information']/p").text

        # Garder uniquement la valeur
        return full_text.replace("Category:", "").strip()
    
    # Localise le prix
    def get_price(self):
        return self.driver.find_element(By.XPATH, "//div[@class='product-information']/span/span")
    
    # Localise la disponibilité
    def get_availability(self):
        # Récupére tout le texte
        full_text = self.driver.find_element(By.XPATH, "//p[b[contains(text(), 'Availability:')]]").text

        # Garder uniquement la valeur
        return full_text.replace("Availability:", "").strip()
    
     # Localise la condition
    def get_condition(self):
        # Récupére tout le texte
        full_text = self.driver.find_element(By.XPATH, "//p[b[contains(text(), 'Condition:')]]").text

        # Garder uniquement la valeur
        return full_text.replace("Condition:", "").strip()
    
     # Localise la marque
    def get_brand(self):
        # Récupére tout le texte
        full_text = self.driver.find_element(By.XPATH, "//p[b[contains(text(), 'Brand:')]]").text

        # Garder uniquement la valeur
        return full_text.replace("Brand:", "").strip()
    
    # Localise la quantité
    def get_quantity(self):
        return self.driver.find_element(By.ID, "quantity")
    
    # Ajout de la quantité
    def add_quantity(self, qte):
        self.get_quantity().clear()
        self.get_quantity().send_keys(qte)
        
    # Clique sur le bouton Add to cart
    def click_add_cart(self):
        # normalize-space() pour ignorer les espaces inutiles et les retours à la ligne présents dans le code HTML
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Add to cart']").click()
        
    # Localise le titre Write Your Review
    def get_title_review(self):
        return self.driver.find_element(By.XPATH, "//a[@href='#reviews']")
    
    # Localise la zone de saisie du nom
    def get_name(self):
        return self.driver.find_element(By.ID, "name")
    
    # Localise la zone de saisie du mail
    def get_email(self):
        return self.driver.find_element(By.ID, "email")
    
    # Localise la zone de saisie de la review
    def get_review(self):
        return self.driver.find_element(By.ID, "review")
    
    # Rempli le formulaire de review
    def fill_review(self, table):

        # Rempli les textbox
        self.get_name().send_keys(table[0]["name"])
        self.get_email().send_keys(table[0]["email"])
        self.get_review().send_keys(table[0]["review"])
        
    # Clique sur le bouton Submit
    def click_submit(self):
        self.driver.find_element(By.ID, "button-review").click()
        
    # Localise le message de succes
    def get_message_success_review(self):
        return self.driver.find_element(By.ID, "review-section")