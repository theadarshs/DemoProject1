from selenium.webdriver.common.by import By


class Addtocart:
    def AddToCart(self):
        Shooos= self.driver.find_elements(By.XPATH,"//div[@class='_1YokD2 _3Mn1Gg']")
        for shoo in Shooos:
            shoo.find_element(By.XPATH,"(//div)[267]").click()

        windowsopen = self.driver.window_handles
        self.driver.switch_to.window(windowsopen[0])

        number = self.driver.find_elements(By.XPATH,"(//ul[@class='_1q8vHb'])[2]")
        for numberss in number:
            numberss.find_element(By.XPATH,"//a[normalize-space()='6']").click()



