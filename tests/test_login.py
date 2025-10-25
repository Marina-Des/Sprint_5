import constants.urls as urls
import constants.credentials as creds
import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:

    # Куда бы пользователь ни нажал - на кнопку "Войти в аккаунт", "Личный кабинет" и прочее перечисленное в задании, он все равно попадет на одну и ту же страницу входа. 
    # Поэтому сейчас идет группа тестов на то, что разные пути приводят на страницу с вводом логина и пароля для входа.
    # А дальше будет один метод - тест самой формы входа. Чтобы тест формы входа не копировать в каждый метод перехода к логину. 


    # вход по кнопке «Войти в аккаунт» на главной,

    def test_login_by_pressing_login_into_account_button_on_main_page(self):
        driver=webdriver.Chrome()
        driver.get(urls.url_main_page)
        WebDriverWait(driver, 3)
        driver.find_element(By.XPATH, '//button[contains(text(),"Войти в аккаунт")]').click()
        WebDriverWait(driver, 3)

        assert ('login' in driver.current_url)

        driver.quit()


    # вход через кнопку «Личный кабинет»,

    def test_login_by_pressing_personal_account_button_not_logged_in(self):
        driver=webdriver.Chrome()
        driver.get(urls.url_main_page)
        WebDriverWait(driver, 3)
        driver.find_element(By.XPATH, '//*[contains(text(), "Личный Кабинет")]/parent::a').click()
        WebDriverWait(driver, 3)

        assert 'login' in driver.current_url

        driver.quit()


    # вход через кнопку в форме регистрации,

    def test_login_through_registration_page(self):
        driver=webdriver.Chrome()
        driver.get(urls.url_registration_page)
        WebDriverWait(driver, 3)
        driver.find_element(By.XPATH, './/a[contains(text(),"Войти")]').click()

        assert ('login' in driver.current_url)

        driver.quit()


    # вход через кнопку в форме восстановления пароля.

    def test_login_through_password_recovery_form(self):
        driver=webdriver.Chrome()
        driver.get(urls.url_password_recovery)
        WebDriverWait(driver, 3)
        driver.find_element(By.XPATH, './/a[contains(text(),"Войти")]').click()

        assert ('login' in driver.current_url)
        
        driver.quit()


    # тестирование входа с данными уже зарегистрированного пользователя

    def test_login_with_correct_credentials (self):
        driver = webdriver.Chrome()
        driver.get(urls.url_login_form)
        WebDriverWait(driver, 3)
        driver.find_element(By.XPATH, '//label[contains(text(),"Email")]/../input').send_keys(creds.cred_email)
        driver.find_element(By.XPATH, '//label[contains(text(),"Пароль")]/../input').send_keys(creds.cred_password)
        driver.find_element(By.XPATH, '//button[contains(text(),"Войти")]').click()
        time.sleep(3)
        WebDriverWait(driver, 6)
        log_in = driver.find_elements(By.XPATH, '//button[contains(text(),"Войти в аккаунт")]')

        assert  (driver.current_url==urls.url_constructor) and (len(log_in)==0)

        driver.quit()





"""
Вход
    Проверь:
    вход по кнопке «Войти в аккаунт» на главной,
    вход через кнопку «Личный кабинет»,
    вход через кнопку в форме регистрации,
    вход через кнопку в форме восстановления пароля.

"""