from selenium.webdriver.common.by import By

class CartPage:
    
    def __init__(self, driver):
        self.driver = driver
        
    # Localise le nom du produit
    def get_name(self, product_id):
        return self.driver.find_element(By.XPATH, f"//tr[@id='product-{product_id}']//td[@class='cart_description']//a")
    
    # Localise le prix du produit
    def get_price(self, product_id):
        return self.driver.find_element(By.XPATH, f"//tr[@id='product-{product_id}']//td[@class='cart_price']/p")
    
    # Localise la quantité du produit
    def get_quantity(self, product_id):
        return self.driver.find_element(By.XPATH, f"//tr[@id='product-{product_id}']//td[@class='cart_quantity']/button")
    
    # Localise le prix total du produit
    def get_total_price(self, product_id):
        return self.driver.find_element(By.XPATH, f"//tr[@id='product-{product_id}']//p[@class='cart_total_price']")
    
    # Clique sur le bouton Proceed To Checkout
    def click_checkout(self):
        self.driver.find_element(By.XPATH, "//a[text()='Proceed To Checkout']").click()
        
    # Clique sur le bouton Register/Login de l'alerte
    def click_register_login(self):
        self.driver.find_element(By.XPATH, "//p//a[@href='/login']").click()
        
    # Vide le panier
    def click_delete_all_products(self):
        elements = self.driver.find_elements(By.CLASS_NAME, "cart_quantity_delete")
        for btn in elements:
            btn.click()
        
    # Localise le texte quand le panier est vide
    def get_empty(self):
        return self.driver.find_element(By.ID, "empty_cart")