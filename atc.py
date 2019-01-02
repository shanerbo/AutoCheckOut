#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.support.ui import Select
import itchat as ic
from selenium.webdriver.support.wait import WebDriverWait as wait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


addr = "https://yeezysupply.com/"
targetSize = "S/M"
driverPath = r"C:\Users\Erbo\Downloads\chromedriver_win32\chromedriver.exe"

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
ic.auto_login(hotReload=True)

shipping = ["xxxxxx@gmail.com","xxxx","xxxx","472 xxxxxx St.","Unit xxxxxx","Nashua","United States","New Hampshire","03063","7814910874"]
shipping1 = ["dummy@gmail.com", "xxxx","xxxx","xxx xxxxxx St.","xxxx xxxxxxx","Nashua","United States","New Hampshire","03063","8787861524"]

allXPATH = ["//*[@id='number']", "//*[@id='name']", "//*[@id='expiry']", "//*[@id='verification_value']"]
creditInfo = ["xxxxxxxxxxx", "xxxx xxxx", "xxxxx", "xxxxxxxx"]


# In[ ]:


driver = webdriver.Chrome(driverPath, options=chrome_options)
driver.get(addr)
notFind = True
while notFind:
    try:
        div = driver.find_element_by_xpath("//*[@id='yeezy-boost-350-v2-static-3m-reflective-soon']/div/div[3]")
        size = div.find_element_by_xpath(".//*[@id='SIZE']")
        size.send_keys(Keys.NULL)
        for i in range(5):
            ic.search_friends(nickName="Erbo_Unchained")[0].send("Yeezy is up")
            time.sleep(0.1)
        break
    except NoSuchElementException:
        time.sleep(15)
        driver.refresh()
Select(size).select_by_visible_text("S/M")
wait(driver, 5).until(EC.element_to_be_clickable((By.NAME, "add")))
purchase = driver.find_element_by_name("add")
time.sleep(0.3)
purchase.click()

time.sleep(0.7)
wait(driver, 3).until(EC.element_to_be_clickable((By.NAME, "checkout")))
checkout = driver.find_element_by_name("checkout")
checkout.click()
driver.find_element_by_name("checkout[email]").send_keys(shipping1[0])
driver.find_element_by_name("checkout[shipping_address][first_name]").send_keys(shipping1[1])
driver.find_element_by_name("checkout[shipping_address][last_name]").send_keys(shipping1[2])
driver.find_element_by_name("checkout[shipping_address][address1]").send_keys(shipping1[3])
driver.find_element_by_name("checkout[shipping_address][address2]").send_keys(shipping1[4])
driver.find_element_by_name("checkout[shipping_address][city]").send_keys(shipping1[5])
Select(driver.find_element_by_id("checkout_shipping_address_country")).select_by_visible_text(shipping1[6])
Select(driver.find_element_by_id("checkout_shipping_address_province")).select_by_visible_text(shipping1[7])
driver.find_element_by_name("checkout[shipping_address][zip]").send_keys(shipping1[8])
driver.find_element_by_name("checkout[shipping_address][phone]").send_keys(shipping1[9])
wait(driver, 3).until(EC.element_to_be_clickable((By.ID, "salesFinal")))
checkBox = driver.find_element_by_id("salesFinal")
checkBox.click()
time.sleep(0.3)
wait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[1]/div[2]/div[2]/form/div[2]/button")))
toPayment = driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/div[2]/form/div[2]/button")
toPayment.click()
wait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[1]/div[2]/div[2]/form/div[2]/button")))
toShip = driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/div[2]/form/div[2]/button")
time.sleep(0.3)
toShip.click()

form = driver.find_elements_by_class_name("card-fields-iframe")
tracker = 0
for i in form:
    driver.switch_to.frame(i)
    filed = driver.find_element_by_xpath(allXPATH[tracker])
    filed.send_keys(creditInfo[tracker])
    tracker += 1
    driver.switch_to.default_content()
    
firstName = driver.find_element_by_id("checkout_billing_address_first_name")
firstName.send_keys("Erbo")

lastName = driver.find_element_by_id("checkout_billing_address_last_name")
lastName.send_keys("Shan")

address = driver.find_element_by_id("checkout_billing_address_address1")
address.send_keys("6461 Telford ave")

address2 = driver.find_element_by_id("checkout_billing_address_address2")
address2.send_keys("#5307")

city = driver.find_element_by_id("checkout_billing_address_city")
city.send_keys("Burnaby")

country = Select(driver.find_element_by_id("checkout_billing_address_country"))
country.select_by_visible_text("Canada")

province = Select(driver.find_element_by_id("checkout_billing_address_province"))
province.select_by_visible_text("British Columbia")

postal = driver.find_element_by_id("checkout_billing_address_zip")
postal.send_keys("V5H 0B7")

phone = driver.find_element_by_id("checkout_billing_address_phone")
phone.send_keys("6047608818")

complete = driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/div[2]/div/form/div[3]/div[1]/button")
complete.send_keys(Keys.ENTER)


# In[ ]:





# In[ ]:





# In[ ]:


#//*[@id="yeezy-boost-350-v2-static-3m-reflective-soon"]/div/div[3]/form[1]/div[2]/
driver = webdriver.Chrome(driverPath, options=chrome_options)
addr = "https://yeezysupply.com"
driver.get(addr)


# In[ ]:


a = driver.find_element_by_xpath("//*[@id='bouclette-socks-three']/div/div[3]")

a.find_element_by_xpath(".//*[@id='SIZE']").text 


# In[ ]:


size = driver.find_element_by_xpath("//*[@id='yeezy-boost-350-v2-static-3m-reflective-soon']/div/div[3]").find_element_by_xpath(".//*[@id='SIZE']")
Select(size).select_by_visible_text("S/M")


# In[ ]:




