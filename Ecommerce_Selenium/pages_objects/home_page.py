from selenium.webdriver.common.by import By

class HomePage:
    
    def __init__(self, driver):
        self.driver = driver

    # Localise le logo   
    def get_logo(self):
        return self.driver.find_element(By.XPATH, "//header//img")
    
    # Clique sur le bouton Test Cases
    def click_test_cases(self):
        self.driver.find_element(By.XPATH, "//a[@href='/test_cases']").click()
        
    # Scroll en bas de page
    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
    # Localise le titre Recommended items   
    def get_title_recommended_items(self):
        return self.driver.find_element(By.XPATH, "//h2[text()='recommended items']")
    
    # Clique sur la flèche située pour remonter
    def click_arrow_up(self):
        self.driver.find_element(By.ID, "scrollUp").click()
        
    # Localise le titre Full-Fledged practice website for Automation Engineers dans le carrousel
    def get_title_full_fledged(self):
        return self.driver.find_element(By.XPATH, "//div[@id='slider-carousel']//div[contains(@class, 'item active')]//h2")
    
    # Scroll en haut de page
    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0);")