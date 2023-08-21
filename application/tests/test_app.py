import pytest
from selenium.webdriver.common.by import By
from application.tests.FAQTest import FAQTest

from selenium import webdriver

@pytest.fixture(scope="module")
def setup():
    print("Initiating chrome driver")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-popup-blocking")

    pytest.driver = webdriver.Chrome(options = chrome_options)

    pytest.driver.get("https://thekraziestkatlady.com/")

    yield pytest.driver
    pytest.driver.close()

def test_kkl_home(setup):
    xpath = '/html/body/app-root/app-home/div/p[1]'
    element = pytest.driver.find_element(By.XPATH, xpath)
    assert(pytest.driver.current_url == "https://thekraziestkatlady.com/home")
    assert(element.text == "Welcome to the website for KKL Rehoming")

def test_faq_click(setup):
    faq_test = FAQTest(pytest.driver)
    assert(faq_test.click_faq().text == "We are located in the Atlantic City area of South Jersey.")

