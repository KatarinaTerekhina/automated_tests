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
HTML5Forms = driver.find_element_by_css_selector("#content > ul > li.post-181.product.type-product.status-publish.product_cat-html.product_tag-html.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.instock.taxable.shipping-taxable.purchasable.product-type-simple > a.woocommerce-LoopProduct-link > h3")
HTML5Forms.click()
HTML = driver.find_element_by_xpath("//*[@id='product-181']/div[2]/h1")
HTML_get_text = HTML.text
assert HTML_get_text == "HTML5 Forms"
if  HTML_get_text == 'HTML5 Forms':
    print('true')
else:    print('false')