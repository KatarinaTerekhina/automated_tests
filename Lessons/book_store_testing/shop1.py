from selenium import webdriver
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
HTML = driver.find_element_by_link_text("HTML")
HTML.click()
#find_elem = len(driver.find_elements_by_xpath('//*[@id="content"]/ul/li[1]/a[1]/h3'))
#print(find_elem)
#items_count = driver.find_elements_by_xpath("//*[@id='woocommerce_product_categories-2']/ul/li[2]/span")
#if len(items_count) == 3:
#    print("Количество товаров: 3")
#else:
#    print("Ошибка. Количество товаров: " + str(len(items_count)))
HTML = driver.find_elements_by_class_name("attachment-shop_catalog.size-shop_catalog.wp-post-image")
assert HTML == 3
if len(HTML) == 3:
    print('Товара 3')
else:
    print('Товара не 3')