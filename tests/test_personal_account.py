#import conftest
import constants.urls as urls
import constants.credentials as creds
import pytest
import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestPersonalAccount:


    # Проверь переход по клику на «Личный кабинет».

    # по кнопке "Личный кабинет" может быть 2 события: переход на страницу логина и переход в личный кабинет. Отличается тем, залогинен ли уже пользователь или нет. Поэтому пишу 2 теста. 


    def test_transition_to_pa_by_clicking_pa_logged_in (self, driver_creation_login_quit):
        driver = driver_creation_login_quit
        driver.find_element(By.XPATH, '//*[contains(text(), "Личный Кабинет")]/parent::a').click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[contains(text(),"Профиль")]')))
        
        assert driver.current_url == urls.url_account


    def test_transition_to_pa_by_clicking_pa__logged_out (self):
        driver=webdriver.Chrome()
        driver.get(urls.url_main_page)
        WebDriverWait(driver, 3)
        driver.find_element(By.XPATH, '//*[contains(text(), "Личный Кабинет")]/parent::a').click()
        WebDriverWait(driver, 3)

        assert (driver.current_url == urls.url_login_form) 

        driver.quit()
        


# Проверь переход из личного кабинета по клику на «Конструктор»

    def test_transition_to_constructor_from_pa_by_click_on_button (self, driver_creation_login_quit):
        driver=driver_creation_login_quit
        driver.find_element(By.XPATH, '//*[contains(text(), "Личный Кабинет")]/parent::a').click()

        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//p[contains(text(), "Конструктор")]//..//..//a'))) 

        driver.find_element(By.XPATH, '//p[contains(text(), "Конструктор")]//..//..//a').click()

        assert driver.current_url == urls.url_constructor



# Проверь переход из личного кабинета по клику на логотип Stellar Burgers

    def test_transition_by_click_on_logo_from_pa (self, driver_creation_login_quit):
        driver=driver_creation_login_quit
        driver.find_element(By.XPATH, '//*[contains(text(), "Личный Кабинет")]/parent::a').click()

        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//div[starts-with(@class, "AppHeader_header__logo")]//a')))

        driver.find_element(By.XPATH, '//div[starts-with(@class, "AppHeader_header__logo")]//a').click()
        WebDriverWait(driver, 3)
        
        assert driver.current_url == urls.url_main_page



# Проверь выход по кнопке «Выйти» в личном кабинете.

    def test_logout (self, driver_creation_login_quit):
        driver=driver_creation_login_quit
        driver.find_element(By.XPATH, '//*[contains(text(), "Личный Кабинет")]/parent::a').click()
        
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Выход")]')))
        driver.find_element(By.XPATH, '//button[contains(text(), "Выход")]').click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Войти")]')))
        
        assert driver.current_url == urls.url_login_form





"""
Переход в личный кабинет 
    Проверь переход по клику на «Личный кабинет».
Переход из личного кабинета в конструктор 
    Проверь переход по клику на «Конструктор» и на логотип Stellar Burgers.

Выход из аккаунта
    Проверь выход по кнопке «Выйти» в личном кабинете.
"""