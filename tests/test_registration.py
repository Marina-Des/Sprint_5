import constants.urls as urls
import pytest
import time
from datetime import datetime
import re


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



class TestRegistrationChrome:

# Во всех тестах предполагаю, что в случае успешной регистрации приложение переводит на страницу .../login



# генерация адреса эл.почты с использованием текущей даты и времени для меня гарантирует, что я не столкнусь с ситуацией, что "такой пользователь уже зарегистрирован" 
    def generate_email(self):
        base=datetime.now()
        return 'usver'+str(base.year)[2:4]+str(base.month)+str(base.day)+'_'+str(base.hour)+str(base.minute)+str(base.second)+str(base.microsecond)[0:2]+'@abvgd.edu'


    # этот код повторяется во всех тестах, но я не смогла загнать его в фикстуру, а потом применить. Надо больше времени и гугла
    def fill_name_email_password_click_register(self, driver, name, email, password):
        driver.find_element(By.XPATH, '//label[contains(text(),"Имя")]/../input').send_keys(name)
        driver.find_element(By.XPATH, '//label[contains(text(),"Email")]/../input').send_keys(email)
        driver.find_element(By.XPATH, '//label[contains(text(),"Пароль")]/../input').send_keys(password)
        driver.find_element(By.XPATH, '//button[contains(text(),"Зарегистрироваться")]').click()



    # -----------------------------------------------------



    # Проверь успешную регистрацию. 
    def test_reg_successful_with_right_name_email_password(self):
        driver=webdriver.Chrome()
        driver.get(urls.url_registration_page)
        self.fill_name_email_password_click_register(driver, 'correct_name', self.generate_email(), '123456789')
        time.sleep(3) # запас на медленный переход. Приложение тормозит

        assert driver.current_url == urls.url_login_form

        driver.quit()



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
    def test_password_six_simbols(self, password, is_correct_password):
        driver=webdriver.Chrome()
        driver.get(urls.url_registration_page)

        self.fill_name_email_password_click_register(driver, 'correct_name', self.generate_email(), password)
        time.sleep(3) # запас на медленный переход. Приложение тормозит

        is_incorrect_password_message=bool(driver.find_elements(By.XPATH, '//*[contains(text(),"Некорректный пароль")]'))
        is_forward_to_login_url=(driver.current_url==urls.url_login_form)

        assert (is_incorrect_password_message!=is_correct_password) and (is_forward_to_login_url==is_correct_password)

        driver.quit()



    # Проверь: поле «Имя» должно быть не пустым; 

    @pytest.mark.parametrize ('name,is_correct', [
        ['',False],
        ['a',True],
        ['asd', True]
    ])
    def test_name_not_empty(self, name, is_correct):
        driver=webdriver.Chrome()
        driver.get(urls.url_registration_page)

        self.fill_name_email_password_click_register(driver, name, self.generate_email(), 'correct_pwd')
        time.sleep(3) # запас на медленный переход

        # судя по логике приложения, если все данные верны, то идет переход на страницу входа (.../login). Если нет, то никакое сообщение не показывается (хотя за это руки оторвать! и к плечам приделать!), просто ничего не происходит. В том числе перехода. А значит, url остается .../register
        assert ('/register' in driver.current_url) != is_correct

        driver.quit()


    # Проверь: в поле Email введён email в формате логин@домен

    # С этим тестом вышла проблемка. При первом прогоне приложение приняло эл.почту в неправильном формате и зарегистрировала с ней пользователей. Дальше надо чистить БД, но у меня такой возможности нет. Но тесты рабочие.
     
    @pytest.mark.parametrize ('email', ['asd', '@.', 'a@b.11'])
    def test_email_wrong_domain_format(self, email):
        driver=webdriver.Chrome()
        driver.get(urls.url_registration_page)
        self.fill_name_email_password_click_register(driver, 'correct_name', email, 'correct_pwd')
        time.sleep(3) # запас на медленный переход. Приложение тормозит

        assert ('/register' in driver.current_url) == True

        driver.quit()






"""
Регистрация
    Проверь:
    Успешную регистрацию. Поле «Имя» должно быть не пустым; в поле Email введён email в формате логин@домен: например, 123@ya.ru. Минимальный пароль — шесть символов.
    Ошибку для некорректного пароля.
    """