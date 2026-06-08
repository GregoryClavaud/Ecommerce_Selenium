import os
import time
from selenium.webdriver.common.by import By

class OrderPlacedPage:
    
    def __init__(self, driver):
        self.driver = driver
    
    # Clique sur le bouton download    
    def click_download(self):
        self.driver.find_element(By.XPATH, "//a[text()='Download Invoice']").click()
        
    # Vérifie si le fichier est téléchargé
    def check_download(self):
        file_path = os.path.join(os.getcwd(), "downloads", "invoice.txt")
        # Attente pour laisser le temps au téléchargement (max 10s)
        timeout = 10
        while not os.path.exists(file_path) and timeout > 0:
            time.sleep(1)
            timeout -= 1
        assert os.path.exists(file_path)
        
    def click_continue(self):
        self.driver.find_element(By.XPATH, "//a[@href='/']").click()