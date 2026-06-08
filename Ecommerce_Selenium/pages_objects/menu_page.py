from selenium.webdriver.common.by import By

class MenuPage:
    
    def __init__(self, driver):
        self.driver = driver

    # Clique sur Signup/Login
    def click_signup_login(self):
        self.driver.find_element(By.XPATH, "//a[@href='/login']").click()
      
    # Clique sur Delete account    
    def click_delete_account(self):
        self.driver.find_element(By.XPATH, "//a[@href='/delete_account']").click()
    
    # Localise le texte 'Logged in as'    
    def get_username_logged(self):
        return self.driver.find_element(By.XPATH, "//a[contains(text(), 'Logged in as')]")
    
    # Clique sur Logout
    def click_logout(self):
        self.driver.find_element(By.XPATH, "//a[@href='/logout']").click()
    
    # Clique sur Contact us
    def click_contact(self):
        self.driver.find_element(By.XPATH, "//a[@href='/contact_us']").click()
        
    # Clique sur Products
    def click_products(self):
        self.driver.find_element(By.XPATH, "//a[@href='/products']").click()
        
    # Clique sur Cart
    def click_cart(self):
        self.driver.find_element(By.XPATH, "//a[@href='/view_cart']").click()