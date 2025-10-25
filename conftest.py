import constants.urls as urls
import constants.credentials as creds
import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



@pytest.fixture()
def driver_creation_login_quit():
   driver=webdriver.Chrome()
   driver.get(urls.url_login_form)
   driver.find_element(By.XPATH, '//label[contains(text(),"Email")]/../input').send_keys(creds.cred_email)
   driver.find_element(By.XPATH, '//label[contains(text(),"Пароль")]/../input').send_keys(creds.cred_password)
   driver.find_element(By.XPATH, '//button[contains(text(),"Войти")]').click()
   
   yield driver

   driver.quit()