import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome("C:\chromedriver\chromedriver.exe")
driver.get("http://practice.automationtesting.in/")
driver.maximize_window()
Shop = driver.find_element_by_link_text("Shop")
Shop.click()
basket = driver.find_element_by_xpath('//*[@id="content"]/ul/li[3]/a[2]')
basket.click()
time.sleep(3)
item = driver.find_element_by_css_selector('#wpmenucartli > a > span.cartcontents')
assert item.text == '1 Item'
price = driver.find_element_by_css_selector('#wpmenucartli > a > span.amount')
assert price.text == '₹280.00'
basket1 = driver.find_element_by_css_selector('#wpmenucartli > a')
basket1.click()
Subtotal = WebDriverWait(driver, 5).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#page-34 > div > div.woocommerce > div > div > table > tbody > tr.cart-subtotal > td > span"), "₹280.00"))
print(Subtotal)
Total = WebDriverWait(driver, 5).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#page-34 > div > div.woocommerce > div > div > table > tbody > tr.order-total > td > strong > span"), "₹294.00"))
print(Total)
