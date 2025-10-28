import constants.urls as urls
import constants.credentials as creds
import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:


    @pytest.mark.parametrize('start_page,link_locator', [
        [urls.url_main_page, '//button[contains(text(),"Войти в аккаунт")]'],
        [urls.url_main_page, '//*[contains(text(), "Личный Кабинет")]/parent::a'],
        [urls.url_main_page+urls.url_part_registration_page, './/a[contains(text(),"Войти")]'],
        [urls.url_main_page+urls.url_part_password_recovery, './/a[contains(text(),"Войти")]']
    ])
    def test_transitions_to_login_page(self, start_page, link_locator):
        driver=webdriver.Chrome()
        driver.get(start_page)
        WebDriverWait(driver,3)
        driver.find_element(By.XPATH, link_locator).click()

        assert (urls.url_part_login_form in driver.current_url)




    # тестирование входа с данными уже зарегистрированного пользователя

    def test_login_with_correct_credentials (self):
        driver = webdriver.Chrome()
        driver.get(urls.url_main_page+urls.url_part_login_form)
        WebDriverWait(driver, 3)
        driver.find_element(By.XPATH, '//label[contains(text(),"Email")]/../input').send_keys(creds.cred_email)
        driver.find_element(By.XPATH, '//label[contains(text(),"Пароль")]/../input').send_keys(creds.cred_password)
        driver.find_element(By.XPATH, '//button[contains(text(),"Войти")]').click()
        time.sleep(3)
        WebDriverWait(driver, 6)
        log_in = driver.find_elements(By.XPATH, '//button[contains(text(),"Войти в аккаунт")]')

        assert  (driver.current_url==(urls.url_main_page+urls.url_part_constructor)) and (len(log_in)==0)

        driver.quit()





"""
Вход
    Проверь:
    вход по кнопке «Войти в аккаунт» на главной,
    вход через кнопку «Личный кабинет»,
    вход через кнопку в форме регистрации,
    вход через кнопку в форме восстановления пароля.

"""