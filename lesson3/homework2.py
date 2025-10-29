from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import pytest


@pytest.fixture
def driver():
    """Фикстура для запуска Firefox"""
    # Если geckodriver уже в PATH — путь указывать не нужно.
    service = Service()
    options = Options()
    # options.add_argument("--headless")  # можно включить, чтобы не открывалось окно браузера

    driver = webdriver.Firefox(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_payment_methods(driver):
    """Тест: открыть сайт, перейти в 'Способы оплаты' и сделать скриншот"""
    driver.get("https://itcareerhub.de/ru")
    sleep(3)

    # Находим и кликаем по ссылке "Способы оплаты"
    payment_link = driver.find_element(By.LINK_TEXT, "Способы оплаты")
    payment_link.click()
    sleep(3)

    # Скриншот всей страницы
    driver.save_screenshot("payment_methods_section.png")
    sleep(2)
