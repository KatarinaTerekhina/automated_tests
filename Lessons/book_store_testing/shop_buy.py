from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome("C:\chromedriver\chromedriver.exe")
driver.get("http://practice.automationtesting.in/")
driver.maximize_window()
Shop = driver.find_element_by_link_text("Shop")
Shop.click()
driver.execute_script("window.scrollBy(0, 300);")
basket = driver.find_element_by_css_selector('#content > ul > li.post-181.product.type-product.status-publish.product_cat-html.product_tag-html.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.instock.taxable.shipping-taxable.purchasable.product-type-simple > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart')
basket.click()
time.sleep(3)
basket1 = driver.find_element_by_css_selector('#wpmenucartli > a')
basket1.click()
CHECKOUT = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#page-34 > div > div.woocommerce > div > div > div > a"))).click()
Name = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#billing_first_name")))
Name1 = driver.find_element_by_id("billing_first_name")
Name1.send_keys("Katrin")
NameL = driver.find_element_by_id("billing_last_name")
NameL.send_keys("Terekhina")
email = driver.find_element_by_id("billing_email")
email.send_keys("demo1@gmail.com")
phone = driver.find_element_by_id("billing_phone")
phone.send_keys("+7-812-44-33-66")
Address = driver.find_element_by_id("billing_address_1")
Address.send_keys("Proletarskay")
Address1 = driver.find_element_by_id("billing_address_2")
Address1.send_keys("13")
Town = driver.find_element_by_id("billing_city")
Town.send_keys("Saint-Petersburg")
country = driver.find_element_by_xpath('//*[@id="s2id_billing_country"]')
country.click()
country1 = driver.find_element_by_id("s2id_autogen1_search")
country1.send_keys("Russia")
country2 = driver.find_element_by_css_selector("#select2-results-1 > li")
country2.click()
State = driver.find_element_by_id("billing_state")
State.send_keys("Russia")
ZIP = driver.find_element_by_id("billing_postcode")
ZIP.send_keys("190000")

driver.execute_script("window.scrollBy(0, 600);")
time.sleep(5)
pay = driver.find_element_by_xpath('//*[@id="payment_method_cheque"]').click()
order = driver.find_element_by_id('place_order')
order.click()
thx = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#page-35 > div > div.woocommerce > p.woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
chek = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#page-35 > div > div.woocommerce > ul > li.method > strong"), "Check Payments"))
