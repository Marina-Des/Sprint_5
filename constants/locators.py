from selenium.webdriver.common.by import By


# локаторы рассортированы по страницам, на которых они находятся. НЕ по файлам использования

# common

common_main_block = [By.XPATH, '//main[contains(@class, "App_componentContainer")]']
common_button = [By.XPATH, '//button']

# constructor page

constr_bulki_head = [By.XPATH, '//h2[contains(text(), "Булки")]']
constr_bulki_tab_header = [By.XPATH, '//span[contains(text(), "Булки")]']
constr_bulki_tab_header_div = [By.XPATH, '//span[contains(text(), "Булки")]/parent::div']
constr_sousy_head = [By.XPATH, '//h2[contains(text(), "Соусы")]']
constr_sousy_tab_header = [By.XPATH, '//span[contains(text(), "Соусы")]']
constr_sousy_tab_header_div = [By.XPATH, '//span[contains(text(), "Соусы")]/parent::div']
constr_nachinki_head = [By.XPATH, '//h2[contains(text(), "Начинки")]']
constr_nachinki_tab_header = [By.XPATH, '//span[contains(text(), "Начинки")]']
constr_nachinki_tab_header_div = [By.XPATH, '//span[contains(text(), "Начинки")]/parent::div']


# login page

login_login_lettering = [By.XPATH, '//h2[contains(text(), "Вход")]']
login_email_input = [By.XPATH, '//label[contains(text(),"Email")]/../input']
login_password_input = [By.XPATH, '//label[contains(text(),"Пароль")]/../input']
login_login_button = [By.XPATH, '//button[contains(text(),"Войти")]']


# main page

main_assemble_a_burger_lettering = [By.XPATH, '//h1[contains(text(), "Соберите бургер")]']
main_login_into_account_button = [By.XPATH, '//button[contains(text(),"Войти в аккаунт")]']
main_personal_account_link = [By.XPATH, '//*[contains(text(), "Личный Кабинет")]/parent::a']


# password recovery page

pasrec_login_link = [By.XPATH, './/a[contains(text(),"Войти")]']


# personal account page

pa_profile_lettering = [By.XPATH, '//*[contains(text(),"Профиль")]']
pa_constructor_link = [By.XPATH, '//p[contains(text(), "Конструктор")]//..//..//a']
pa_logo_link = [By.XPATH, '//div[starts-with(@class, "AppHeader_header__logo")]//a']
pa_quit_button = [By.XPATH, '//button[contains(text(), "Выход")]']


# registration page

reg_login_link = [By.XPATH, './/a[contains(text(),"Войти")]']
reg_name_input = [By.XPATH, '//label[contains(text(),"Имя")]/../input']
reg_email_input = [By.XPATH, '//label[contains(text(),"Email")]/../input']
reg_password_input = [By.XPATH, '//label[contains(text(),"Пароль")]/../input']
reg_register_button = [By.XPATH, '//button[contains(text(),"Зарегистрироваться")]']
reg_incorrect_password_message = [By.XPATH, '//*[contains(text(),"Некорректный пароль")]']




        # WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[contains(text(),"Профиль")]')))
        
        # WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//p[contains(text(), "Конструктор")]//..//..//a'))) 

        # WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//div[starts-with(@class, "AppHeader_header__logo")]//a')))



