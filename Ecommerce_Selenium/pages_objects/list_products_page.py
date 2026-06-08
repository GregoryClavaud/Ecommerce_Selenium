from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ListProductsPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
    
    # Localise la liste des produits  
    def get_list_products(self):
        return self.driver.find_elements(By.CLASS_NAME, "product-image-wrapper")
    
    # Localise un produit
    def get_product(self, product):
        return self.driver.find_element(By.CLASS_NAME, "single-products")
    
    # Clique sur le bouton View Product
    def click_view_product(self, product_id):
        self.driver.find_element(By.XPATH, f"//a[@href='/product_details/{product_id}']").click()
        
    # Clique sur le bouton add to cart
    def click_add_cart(self, product_id):
        self.driver.find_element(By.XPATH, f"//a[@data-product-id='{product_id}']").click()
        
    # Clique sur le bouton continue shopping
    def click_continue_shopping(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Continue Shopping']"))).click()
        
    # Clique sur le bouton view cart
    def click_view_cart(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='cartModal']//u[text()='View Cart']"))).click()