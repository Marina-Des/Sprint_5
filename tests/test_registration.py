import constants.urls as urls
import constants.locators as locs
import pytest
import time
import re
import random
import string


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



class TestRegistrationChrome:

# тут должны упасть 2 теста - на пустом вводе пароля и на вводе адреса эл.почты с доменом первого уровня в виде числа

# Во всех тестах предполагаю, что в случае успешной регистрации приложение переводит на страницу .../login


    def generate_correct_email(self):
        return 'usver'+ str(int(random.random()*10000))+'@abvgd.edu'


    # этот код повторяется во всех тестах, но я не смогла загнать его в фикстуру, а потом применить. Надо больше времени и гугла
    def fill_name_email_password_click_register(self, driver, name, email, password):
        driver.find_element(*locs.reg_name_input).send_keys(name)
        driver.find_element(*locs.reg_email_input).send_keys(email)
        driver.find_element(*locs.reg_password_input).send_keys(password)
        driver.find_element(*locs.reg_register_button).click()


    def wait_for_loading_main_presence(self, driver):
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(locs.common_main_block))


    # -----------------------------------------------------



    # Проверь успешную регистрацию. 
    def test_reg_successful_with_right_name_email_password(self, driver_creation_quit):
        driver = driver_creation_quit
        driver.get(urls.url_main_page+urls.url_part_registration_page)
        self.fill_name_email_password_click_register(driver, 'correct_name', self.generate_correct_email(), '123456789')
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locs.login_login_lettering))     

        assert (urls.url_part_login_form in driver.current_url)




    # Пароль — шесть символов. Проверь ошибку для некорректного пароля.

    # Здесь предполагаю, что при нажатии кнопки "Зарегистрироваться" при неправильно введенном пароле должна появляться надпись "Некорректный пароль". 

    #Проверяем значения количества символов на границах и внутри. 
    @pytest.mark.parametrize ('password,is_correct_password', [
        ['', False], 
        ['1', False], 
        ['123', False],
        ['12345', False], 
        ['123456', True], 
        ['1234567', True],
        ['1234567890', True]])
    def test_password_six_simbols(self, password, is_correct_password, driver_creation_quit):
        driver = driver_creation_quit
        driver.get(urls.url_main_page+urls.url_part_registration_page)

        self.fill_name_email_password_click_register(driver, 'correct_name', self.generate_correct_email(), password)

        if is_correct_password:
            WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locs.login_login_lettering))
        else:
            WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locs.reg_incorrect_password_message))

        is_incorrect_password_message=bool(driver.find_elements(*locs.reg_incorrect_password_message))
        is_forward_to_login_url=(urls.url_part_login_form in driver.current_url)

        assert (is_incorrect_password_message!=is_correct_password) and (is_forward_to_login_url==is_correct_password)



    # Проверь: поле «Имя» должно быть не пустым; 

    @pytest.mark.parametrize ('name,is_correct', [
        ['',False],
        ['a',True],
        ['asd', True]
    ])
    def test_name_not_empty(self, name, is_correct, driver_creation_quit):
        driver = driver_creation_quit
        driver.get(urls.url_main_page+urls.url_part_registration_page)

        self.fill_name_email_password_click_register(driver, name, self.generate_correct_email(), 'correct_pwd')

        if is_correct:
            WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locs.login_login_lettering))

        # судя по логике приложения, если все данные верны, то идет переход на страницу входа (.../login). Если нет, то никакое сообщение не показывается (хотя за это руки оторвать! и к плечам приделать!), просто ничего не происходит. В том числе перехода. А значит, url остается .../register
        assert (urls.url_part_registration_page in driver.current_url) != is_correct



    # Проверь: в поле Email введён email в формате логин@домен

    # Генерация некорректного адреса эл.почты состоит из 4х частей: имя, количество @, домен 2 уровня и "хвост" - домен 1го уровня и . , если есть. Любая часть может состоять из указываемого количества символов от 0 до лимитов языка. В данном случае я пометила, какие шаблоны генерируются и проверяются, "*" - любая строчная латинская буква. При необходимости - появлении ограничений на символы - можно написать вставку спецсимволов и букв других алфавитов при необходимости. 
     
    @pytest.mark.parametrize ('name,at,domain2,tail', [
        [0, 0, 0, ''],   # пустая строка
        [4, 0, 0, ''],   # ****
        [4, 0, 0, '.org'],   # ****.org
        [0, 1, 4, ''],   # @****
        [0, 1, 4, '.org'],   # @****.org
        [5, 1, 4,'.11'],   # *****@****.11
        [5, 1, 4, '.']   # *****@****.
        ])
    def test_email_wrong_domain_format(self, name, at, domain2, tail, driver_creation_quit):
        driver = driver_creation_quit
        driver.get(urls.url_main_page+urls.url_part_registration_page)        
        inc_email=''.join([random.choice(string.ascii_lowercase) for _ in range(name)])+'@'*at+''.join([random.choice(string.ascii_lowercase) for _ in range(domain2)])+tail

        self.fill_name_email_password_click_register(driver, 'correct_name', inc_email, 'correct_pwd')

        assert (urls.url_part_registration_page in driver.current_url) == True






"""
Регистрация
    Проверь:
    Успешную регистрацию. Поле «Имя» должно быть не пустым; в поле Email введён email в формате логин@домен: например, 123@ya.ru. Минимальный пароль — шесть символов.
    Ошибку для некорректного пароля.
    """