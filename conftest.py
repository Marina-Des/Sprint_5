import pytest

from selenium import webdriver



@pytest.fixture()
def driver_creation_quit():
   driver=webdriver.Chrome()
   
   yield driver

   driver.quit()


