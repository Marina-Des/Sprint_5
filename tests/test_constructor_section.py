import constants.urls as urls
import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestConstructor:

# В этом классе тесты основаны на том, насколько близко после нажатия кнопок перехода к разделу находятся верх окна с разделами и скроллом и верх заголовка соответствующего раздела. По-хорошему, надо смотреть дизайн, я допустила разницу по высоте в 100px. 



    # Проверь, что работает переход к разделу "Булки"
    # Так как булки по умолчанию и так сверху, то сначала прокрутим окно вниз, чтобы потом перейти к булкам и проверить факт движения.
    def test_transition_to_bulki (self):
        driver=webdriver.Chrome()
        driver.get(urls.url_constructor)
        WebDriverWait(driver, 3)
        scroll_frame = driver.find_element(By.XPATH, '//div[contains(@class, "BurgerIngredients_ingredients__menuContainer")]')
        head_bulki = driver.find_element(By.XPATH, '//h2[contains(text(), "Булки")]')
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_frame)
        time.sleep(2)
        WebDriverWait(driver, 3)
        driver.find_element(By.XPATH, '//span[contains(text(), "Булки")]').click()
        time.sleep(2)

        top_scroll = driver.execute_script("""const rect = arguments[0].getBoundingClientRect(); return rect.top; """, scroll_frame)
        top_bulki_new = driver.execute_script("""const rect = arguments[0].getBoundingClientRect(); return rect.top; """, head_bulki)

        assert (top_scroll-top_bulki_new) <=100

        driver.quit()




    # Проверь, что работает переход к разделу "Соусы"
    def test_transition_to_sousy (self):
        driver=webdriver.Chrome()
        driver.get(urls.url_constructor)
        WebDriverWait(driver, 5)
        scroll_frame = driver.find_element(By.XPATH, '//div[contains(@class, "BurgerIngredients_ingredients__menuContainer")]')
        head_sousy = driver.find_element(By.XPATH, '//h2[contains(text(), "Соусы")]')
        
        driver.find_element(By.XPATH, '//span[contains(text(), "Соусы")]').click()
        time.sleep(2)

        top_scroll = driver.execute_script("""const rect = arguments[0].getBoundingClientRect(); return rect.top; """, scroll_frame)
        top_sousy_new = driver.execute_script("""const rect = arguments[0].getBoundingClientRect(); return rect.top; """, head_sousy)

        assert (top_scroll-top_sousy_new) <=100

        driver.quit()



    # Проверь, что работает переход к разделу "Начинки"
    def test_transition_to_nachinki (self):
        driver=webdriver.Chrome()
        driver.get(urls.url_constructor)

        scroll_frame = driver.find_element(By.XPATH, '//div[contains(@class, "BurgerIngredients_ingredients__menuContainer")]')
        head_nachinki = driver.find_element(By.XPATH, '//h2[contains(text(), "Начинки")]')

        driver.find_element(By.XPATH, '//span[contains(text(), "Начинки")]').click()
        time.sleep(2)

        top_scroll = driver.execute_script("""const rect = arguments[0].getBoundingClientRect(); return rect.top; """, scroll_frame)
        top_nachinki_new = driver.execute_script("""const rect = arguments[0].getBoundingClientRect(); return rect.top; """, head_nachinki)

        assert (top_scroll-top_nachinki_new) <=100

        driver.quit()





"""
Раздел «Конструктор»
    Проверь, что работают переходы к разделам:
    «Булки»,
    «Соусы»,
    «Начинки».
"""