from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchProductPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        
    # Localise la zone de saisie du produit recherché
    def get_search(self):
        return self.driver.find_element(By.ID, "search_product")
    
    # Rempli la zone de saisie
    def fill_search(self, table):
        self.get_search().send_keys(table[0]["search product"])
        
    # Clique sur le bouton search
    def click_search(self):
        self.driver.find_element(By.ID, "submit_search").click()
    
    # Loclaise le titre de la page    
    def get_titre(self):
        return self.driver.find_element(By.XPATH, "//h2[text()='Searched Products']")
    
    # Localise le titre categorie
    def get_category(self):
        return self.driver.find_element(By.XPATH, "//h2[text()='Category']")
    
    # Clique sur la catégorie Women
    def click_women_category(self):
        self.driver.find_element(By.XPATH, "//a[@href='#Women']").click()
        
    # Clique sur la sous catégorie Tops de Women
    def click_sub_women_category(self, sub_category):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//a[@href='/category_products/{sub_category}']"))).click()
        
    # Localise le titre de la sous catégorie
    def get_title_sub_category(self):
        return self.driver.find_element(By.XPATH, "//h2[@class='title text-center']")
    
    # Clique sur la catégorie Men
    def click_men_category(self):
        self.driver.find_element(By.XPATH, "//a[@href='#Men']").click()
        
    # Clique sur la sous catégorie Tshirts de Men
    def click_sub_men_category(self, sub_category):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//a[@href='/category_products/{sub_category}']"))).click()
        
    # Localise le titre categorie
    def get_brand(self):
        return self.driver.find_element(By.XPATH, "//h2[text()='Brands']")
    
    # Clique sur la sous marque
    def click_sub_brand(self, sub_brand):
        self.driver.find_element(By.XPATH, f"//a[@href='/brand_products/{sub_brand}']").click()