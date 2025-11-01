import constants.urls as urls
import constants.locators as locs
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestConstructor:

    class_tab_header_selected = 'tab_tab_type_current'

    # Проверь, что работает переход к разделу "Булки"


    def test_transition_to_bulki (self, driver_creation_quit):
        driver=driver_creation_quit
        driver.get(urls.url_main_page+urls.url_part_constructor)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locs.constr_nachinki_tab_header))

        driver.find_element(*locs.constr_nachinki_tab_header).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(locs.constr_bulki_tab_header))

        status_before = (self.class_tab_header_selected in driver.find_element(*locs.constr_bulki_tab_header_div).get_attribute('class'))
        # must be False

        driver.find_element(*locs.constr_bulki_tab_header).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(locs.constr_nachinki_tab_header))

        status_after = (self.class_tab_header_selected in driver.find_element(*locs.constr_bulki_tab_header_div).get_attribute('class'))


        assert (not status_before) and (status_after)




    # Проверь, что работает переход к разделу "Соусы"
    def test_transition_to_sousy (self, driver_creation_quit):
        driver=driver_creation_quit
        driver.get(urls.url_main_page+urls.url_part_constructor)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locs.constr_sousy_tab_header))

        status_before = (self.class_tab_header_selected in driver.find_element(*locs.constr_sousy_tab_header_div).get_attribute('class'))
        # must be False

        driver.find_element(*locs.constr_sousy_tab_header).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(locs.constr_bulki_tab_header))
        status_after = (self.class_tab_header_selected in driver.find_element(*locs.constr_sousy_tab_header_div).get_attribute('class'))
    
        assert (not status_before) and (status_after)




    # Проверь, что работает переход к разделу "Начинки"
    def test_transition_to_nachinki (self, driver_creation_quit):
        driver=driver_creation_quit
        driver.get(urls.url_main_page+urls.url_part_constructor)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locs.constr_nachinki_tab_header))
        status_before = (self.class_tab_header_selected in driver.find_element(*locs.constr_nachinki_tab_header_div).get_attribute('class'))
        # must be False

        driver.find_element(*locs.constr_nachinki_tab_header).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(locs.constr_nachinki_tab_header))
        status_after = (self.class_tab_header_selected in driver.find_element(*locs.constr_nachinki_tab_header_div).get_attribute('class'))

        assert (not status_before) and (status_after)





"""
Раздел «Конструктор»
    Проверь, что работают переходы к разделам:
    «Булки»,
    «Соусы»,
    «Начинки».
"""