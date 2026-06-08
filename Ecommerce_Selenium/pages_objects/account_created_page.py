from selenium.webdriver.common.by import By

class AccountCreatedPage:
    
    def __init__(self, driver):
        self.driver = driver
      
    # Localise le titre    
    def get_titre(self):
        return self.driver.find_element(By.XPATH, "//b[text()='Account Created!']")
    
    # Clique sur le bouton Continue
    def click_continue(self):
        self.driver.find_element(By.XPATH, "//a[text()='Continue']").click()