from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome("C:\chromedriver\chromedriver.exe")
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
time.sleep(5)
Android = driver.find_element_by_css_selector("#content > ul > li.post-169.product.type-product.status-publish.product_cat-android.product_tag-android.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.first.outofstock.sale.downloadable.taxable.shipping-taxable.purchasable.product-type-simple > a.woocommerce-LoopProduct-link > h3")
Android.click()
oldprice = driver.find_element_by_css_selector('#product-169 > div.summary.entry-summary > div:nth-child(2) > p > del > span')
assert oldprice.text == '₹600.00'
newprice = driver.find_element_by_css_selector('#product-169 > div.summary.entry-summary > div:nth-child(2) > p > ins > span')
assert newprice.text == '₹450.00'
cover = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='product-169']/div[1]/a/img"))).click()
close = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.pp_pic_holder.pp_woocommerce > div.pp_content_container > div > div > div > div.pp_fade > div.pp_details > a"))).click()

