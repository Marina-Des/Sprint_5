import constants.urls as urls
import constants.credentials as creds
import constants.locators as locs
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait




@pytest.fixture()
def driver_creation_quit():
   driver=webdriver.Chrome()
   
   yield driver

   driver.quit()


@pytest.fixture()
def driver_creation_login_quit(driver_creation_quit):
   driver=driver_creation_quit
   driver.get(urls.url_main_page+urls.url_part_login_form)
   driver.find_element(*locs.login_email_input).send_keys(creds.cred_email)
   driver.find_element(*locs.login_password_input).send_keys(creds.cred_password)
   driver.find_element(*locs.login_login_button).click()
   
   yield driver

