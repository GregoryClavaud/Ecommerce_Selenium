from selenium.webdriver.common.by import By

class DeletedAccountPage:
    
    def __init__(self, driver):
        self.driver = driver
        
    # Localise le titre    
    def get_titre(self):
        return self.driver.find_element(By.XPATH, "//h2/b[text()='Account Deleted!']")
    
    # Clique sur le bouton Continue
    def click_continue(self):
        self.driver.find_element(By.XPATH, "//a[text()='Continue']").click()