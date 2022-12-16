import time


from selenium.webdriver.common.by import By

class SearchPage:

    def search(self):
        #self.driver.find_element(By.CSS_SELECTOR,"button[class ='_2KpZ6l _2doB4z']").click()
        self.driver.find_element(By.NAME,"q").send_keys("shoes for men")
        shoes = self.driver.find_elements(By.XPATH,"//ul[@class='col-12-12 _1MRYA1 _38UFBk']")
        time.sleep(3)
        for shoe in shoes:
            shoe.find_element(By.XPATH, "(//a[@class='_3izBDY'])[1]").click()
        time.sleep(5)