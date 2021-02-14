import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome("C:\chromedriver\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
driver.maximize_window()
driver.execute_script("window.scrollBy(0, 1000);")
time.sleep (5)
Ruby = driver.find_element_by_css_selector("#text-22-sub_row_1-0-2-0-0 > div > ul > li > a.woocommerce-LoopProduct-link > h3")
Ruby.click()
REVIEWS = driver.find_element_by_xpath("//*[@id='product-160']/div[3]/ul/li[2]/a")
REVIEWS.click()
star = driver.find_element_by_css_selector('#commentform > p.comment-form-rating > p > span > a.star-5')
star.click()
Review = driver.find_element_by_id("comment")
Review.send_keys("Nice book!")
Name= driver.find_element_by_id("author")
Name.send_keys("Katrin")
Email = driver.find_element_by_id("email")
Email.send_keys("demo@gmail.com")
SUBMIT = driver.find_element_by_id("submit")
SUBMIT.click()