import constants.urls as urls
import constants.credentials as creds
import constants.locators as locs
import pytest

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:


    @pytest.mark.parametrize('start_page,locator', [
        [urls.url_main_page, locs.main_login_into_account_button],
        [urls.url_main_page, locs.main_personal_account_link],
        [urls.url_main_page+urls.url_part_registration_page, locs.reg_login_link],
        [urls.url_main_page+urls.url_part_password_recovery, locs.pasrec_login_link]
    ])
    def test_transitions_to_login_page(self, start_page, locator, driver_creation_quit):
        driver=driver_creation_quit
        driver.get(start_page)
        driver.find_element(*locator).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(locs.login_login_button))

        assert (urls.url_part_login_form in driver.current_url)




    # тестирование входа с данными уже зарегистрированного пользователя

    def test_login_with_correct_credentials (self, driver_creation_quit):
        driver=driver_creation_quit
        driver.get(urls.url_main_page+urls.url_part_login_form)
        WebDriverWait(driver, 3)
        driver.find_element(*locs.login_email_input).send_keys(creds.cred_email)
        driver.find_element(*locs.login_password_input).send_keys(creds.cred_password)
        driver.find_element(*locs.login_login_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(locs.main_assemble_a_burger_lettering))

        log_in = driver.find_elements(*locs.main_login_into_account_button)

        assert  (driver.current_url==(urls.url_main_page+urls.url_part_constructor)) and (len(log_in)==0)






"""
Вход
    Проверь:
    вход по кнопке «Войти в аккаунт» на главной,
    вход через кнопку «Личный кабинет»,
    вход через кнопку в форме регистрации,
    вход через кнопку в форме восстановления пароля.

"""