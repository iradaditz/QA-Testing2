from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import pytest


@pytest.fixture
def driver():
    
    service = Service()
    options = Options()
   

    driver = webdriver.Firefox(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_payment_methods(driver):
    """Тест: открыть сайт, перейти в 'Способы оплаты' и сделать скриншот"""
    driver.get("https://itcareerhub.de/ru")
    sleep(3)

    
    payment_link = driver.find_element(By.LINK_TEXT, "Способы оплаты")
    payment_link.click()
    sleep(3)

    
    driver.save_screenshot("payment_methods_section.png")    # Скриншот всей страницы
    sleep(2)
