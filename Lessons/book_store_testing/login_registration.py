import time
from selenium import webdriver
driver = webdriver.Chrome("C:\chromedriver\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
driver.maximize_window()
mainMenu = driver.find_element_by_link_text("My Account")
mainMenu.click()
Email = driver.find_element_by_id("reg_email")
Email.send_keys("demo1@gmail.com")
Password = driver.find_element_by_id("reg_password")
Password.send_keys("DolceVita1`59!")
Register = driver.find_element_by_css_selector("#customer_login > div.u-column2.col-2 > form > p.woocomerce-FormRow.form-row > input.woocommerce-Button.button")
Register.click()

