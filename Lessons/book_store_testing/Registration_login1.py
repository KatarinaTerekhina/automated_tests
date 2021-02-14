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
try:
    Logout = driver.find_element_by_xpath('//*[@id="page-36"]/div/div[1]/nav/ul/li[6]/a').get_attribute('Logout')
    print ("Есть элемент")
except:
    print ("Нет элемента")
driver.quit()