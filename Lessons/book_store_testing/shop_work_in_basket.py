from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome("C:\chromedriver\chromedriver.exe")
driver.get("http://practice.automationtesting.in/ ")
driver.maximize_window()
Shop = driver.find_element_by_link_text("Shop")
Shop.click()
driver.execute_script("window.scrollBy(0, 300);")
basket = driver.find_element_by_css_selector('#content > ul > li.post-181.product.type-product.status-publish.product_cat-html.product_tag-html.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.instock.taxable.shipping-taxable.purchasable.product-type-simple > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart')
basket.click()
time.sleep(3)
addbasket = driver.find_element_by_css_selector('#content > ul > li.post-165.product.type-product.status-publish.product_cat-javascript.product_tag-javascript.product_tag-mastering.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.instock.downloadable.taxable.shipping-taxable.purchasable.product-type-simple > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart')
addbasket .click()
basket1 = driver.find_element_by_css_selector('#wpmenucartli > a')
basket1.click()
time.sleep(3)
delete = driver.find_element_by_css_selector('#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(1) > td.product-remove > a')
delete.click()
time.sleep(3)
Undo = driver.find_element_by_css_selector('#page-34 > div > div.woocommerce > div.woocommerce-message > a')
Undo.click()
element = driver.find_element_by_css_selector('#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(1) > td.product-quantity > div > input')
element.clear()
quantity = driver.find_element_by_css_selector("#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(1) > td.product-quantity > div > input")
quantity.send_keys("3")
UPDATEBASKET = driver.find_element_by_css_selector('#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(3) > td > input.button')
UPDATEBASKET.click()
item = driver.find_element_by_css_selector('#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(1) > td.product-quantity > div > input').get_attribute('value')
assert item == "3"
print(item)
time.sleep(3)
APPLYCOUPON = driver.find_element_by_css_selector('#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(3) > td > div > input.button')
APPLYCOUPON.click()
Code = WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#page-34 > div > div.woocommerce > ul"), "Please enter a coupon code."))
