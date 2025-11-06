import constants.urls as urls
import constants.locators as locs
import constants.credentials as creds
import pytest

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestPersonalAccount:


    def login_on_login_page (self, driver):
        driver.get(urls.url_main_page+urls.url_part_login_form)
        driver.find_element(*locs.login_email_input).send_keys(creds.cred_email)
        driver.find_element(*locs.login_password_input).send_keys(creds.cred_password)
        driver.find_element(*locs.login_login_button).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locs.main_assemble_a_burger_lettering))



    # Проверь переход по клику на «Личный кабинет».

    # по кнопке "Личный кабинет" может быть 2 события: переход на страницу логина и переход в личный кабинет. Отличается тем, залогинен ли уже пользователь или нет. Поэтому пишу 2 теста. 


    def test_transition_to_pa_by_clicking_pa_logged_in (self, driver_creation_quit):
        driver = driver_creation_quit
        self.login_on_login_page(driver)
        driver.find_element(*locs.main_personal_account_link).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locs.pa_profile_lettering))
        
        assert (urls.url_part_account in driver.current_url)


    def test_transition_to_pa_by_clicking_pa__logged_out (self, driver_creation_quit):
        driver=driver_creation_quit
        driver.get(urls.url_main_page)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locs.main_personal_account_link))
        driver.find_element(*locs.main_personal_account_link).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locs.login_login_lettering))

        assert (urls.url_part_login_form in driver.current_url) 
        


# Проверь переход из личного кабинета по клику на «Конструктор»

    def test_transition_to_constructor_from_pa_by_click_on_button (self, driver_creation_quit):
        driver=driver_creation_quit
        self.login_on_login_page(driver)
        driver.find_element(*locs.main_personal_account_link).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((locs.pa_constructor_link))) 

        driver.find_element(*locs.pa_constructor_link).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((locs.main_assemble_a_burger_lettering))) 
        
        assert driver.current_url == urls.url_main_page+urls.url_part_constructor



# Проверь переход из личного кабинета по клику на логотип Stellar Burgers

    def test_transition_by_click_on_logo_from_pa (self, driver_creation_quit):
        driver=driver_creation_quit
        self.login_on_login_page(driver)
        driver.find_element(*locs.main_personal_account_link).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((locs.pa_logo_link)))

        driver.find_element(*locs.pa_logo_link).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locs.main_assemble_a_burger_lettering))
        
        assert driver.current_url == urls.url_main_page



# Проверь выход по кнопке «Выйти» в личном кабинете.

    def test_logout (self, driver_creation_quit):
        driver=driver_creation_quit
        self.login_on_login_page(driver)
        driver.find_element(*locs.main_personal_account_link).click()
        
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((locs.pa_quit_button)))
        driver.find_element(*locs.pa_quit_button).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((locs.login_login_button)))
        
        assert (urls.url_part_login_form in driver.current_url)





"""
Переход в личный кабинет 
    Проверь переход по клику на «Личный кабинет».
Переход из личного кабинета в конструктор 
    Проверь переход по клику на «Конструктор» и на логотип Stellar Burgers.

Выход из аккаунта
    Проверь выход по кнопке «Выйти» в личном кабинете.
"""