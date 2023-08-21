from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

class FAQTest:
    def __init__(self, driver):
        self.driver = driver

    def click_faq(self):
        faq_link = "//*[@id=\"myTopnav\"]/a[11]"
        button_xpath = "/html/body/app-root/app-faq/div/button[1]"
        text_xpath = "/html/body/app-root/app-faq/div/div[1]/p"

        faq_page = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, faq_link))
        )

        faq_page.click()
        time.sleep(2)

        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, button_xpath))
        )

        element.click()
        time.sleep(2)

        element2 = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, text_xpath))
        )
  
        print("[+] FAQ click successful")

        return element2