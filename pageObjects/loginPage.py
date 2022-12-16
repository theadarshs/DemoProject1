from selenium.webdriver.common.by import By

from tests import test_e2e


class LoginPage:

    def login(self):
        #self.driver.find_element(By.CSS_SELECTOR,"[class='_2IX_2- VJZDxU']").send_keys("6265445594")
        #self.driver.find_element(By.XPATH,"//input[@type='password']").send_keys("Adarsh1997")
        #self.driver.find_element(By.XPATH,"//button[@class='_2KpZ6l _2HKlqd _3AWRsL']").click()
        self.driver.find_element(By.CSS_SELECTOR,"[class ='_2KpZ6l _2doB4z']").click()