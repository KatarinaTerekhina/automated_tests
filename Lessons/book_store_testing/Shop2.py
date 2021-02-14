from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome("C:\chromedriver\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
driver.maximize_window()
mainMenu = driver.find_element_by_link_text("My Account")
mainMenu.click()
LoginEmail = driver.find_element_by_id("username")
LoginEmail.send_keys("demo1@gmail.com")
LoginPassword = driver.find_element_by_id("password")
LoginPassword.send_keys("DolceVita1`59!")
Login = driver.find_element_by_css_selector("#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > input.woocommerce-Button.button")
Login.click()
Shop = driver.find_element_by_link_text("Shop")
Shop.click()
price = driver.find_element_by_css_selector("[value='price-desc']")
if price == 'Sort by price: high to low':
    print('Вариант сортировки от большего к меньшему')
else:
    print('Вариант сортировки не от большего к меньшему')
select = Select(driver.find_element_by_class_name("orderby")) #Открываем список через Select
select.select_by_value('price-desc') #Выбираем нужное нам значение по value
time.sleep(5)
price1 = driver.find_element_by_css_selector("[value='menu_order']").click()
price2 = driver.find_element_by_css_selector("[value='price-desc']")
if price2 == 'Sort by price: high to low':
    print('Вариант сортировки от большего к меньшему')
else:
    print('Вариант сортировки не от большего к меньшему')
