
# coding: utf-8

# In[1]:


import requests
import http.cookiejar as cookielib
import urllib
import io
from bs4 import BeautifulSoup as bs
import re


# In[152]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait as wait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


# In[153]:


addr = "https://yeezysupply.com/products/flannel-lined-canvas-jacket-medium-blue?c=%2Fcollections%2Fnew-arrivals-outerwear"
targetSize = "XL"
driverPath = r"/Users/Unchained_Erbo/Downloads/chromedriver"

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_dfault_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(driverPath, options=chrome_options)
driver.get(addr)


# In[169]:


size = driver.find_element_by_id("SIZE")
Select(size).select_by_visible_text(targetSize)
wait(driver, 3).until(EC.element_to_be_clickable((By.NAME, "add")))
purchase = driver.find_element_by_name("add")
time.sleep(0.3)
purchase.click()


# In[170]:


checkout = driver.find_element_by_name("checkout")
checkout.click()


# In[156]:


cookieDict = {}
for i in driver.get_cookies():
    cookieDict[i['name']] = i['value']


# In[157]:


for i in sorted(cookieDict):
    print( i + " : " + cookieDict[i])


# In[158]:


len(cookieDict)


# In[159]:


s =  requests.Session()


# In[160]:


c = [s.cookies.set(c['name'], c['value']) for c in driver.get_cookies()]


# In[161]:


userAgent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
rootUrl = "https://yeezysupply.com"
postData = {
    'id': "12605134995555", 
    'quantity': '2', 
    'properties': {}
}
header = {
    "Referer": rootUrl,
    "User-Agent": userAgent
}
response = s.post("https://yeezysupply.com/cart/add.js", data = postData, headers = header)
print("statusCode = " + str(response.status_code))
print("text = " + response.text)


# In[162]:


response.url


# In[163]:


checkoutUrl = "https://yeezysupply.com/cart"
postData = {
    "updates%5B%5D": 2,
    'update': 'UPDATE CART',
    "checkout": "CHECKOUT",
}
response = s.post(checkoutUrl, data = postData, headers = header, allow_redirects=True)
print("statusCode = " + str(response.status_code))
print("text = " + response.text)


# In[164]:


shippingRequestUrl = response.url


# In[165]:


ga = s.cookies.get_dict()['_shopify_ga']


# In[166]:


beautifyHTML = bs(response.text, "html.parser")
beautyfiedHTML = beautifyHTML.find_all('form', {'class': 'edit_checkout'})[0]
authenticity_token = beautyfiedHTML.find(attrs = {'name': "authenticity_token"})['value']


# In[167]:


authenticity_token


# In[173]:


driver.get(shippingRequestUrl)


# In[150]:


a = s.get(shippingRequestUrl)


# In[ ]:





# In[ ]:





# In[ ]:





# In[144]:


userAgent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
header = {
    "Referer": shippingRequestUrl ,
    "User-Agent": userAgent
}
postData = {
    'utf8': '%E2%9C%93',
    '_method': 'patch',
    'authenticity_token': '',
    'previous_step': 'contact_information',
    'step': 'shipping_method',
    'checkout%5Bemail%5D': 'dummy%40gmail.com',
    'checkout%5Bbuyer_accepts_marketing%5D': '0',
    'checkout%5Bshipping_address%5D%5Bfirst_name%5D': '',
    'checkout%5Bshipping_address%5D%5Blast_name%5D': '',
    'checkout%5Bshipping_address%5D%5Baddress1%5D': '',
    'checkout%5Bshipping_address%5D%5Baddress2%5D': '',
    'checkout%5Bshipping_address%5D%5Bcity%5D': '',
    'checkout%5Bshipping_address%5D%5Bcountry%5D': '',
    'checkout%5Bshipping_address%5D%5Bprovince%5D': '',
    'checkout%5Bshipping_address%5D%5Bzip%5D': '',
    'checkout%5Bshipping_address%5D%5Bphone%5D': '',
    'checkout%5Bshipping_address%5D%5Bfirst_name%5D': '11',
    'checkout%5Bshipping_address%5D%5Blast_name%5D': '11',
    'checkout%5Bshipping_address%5D%5Baddress1%5D': '11',
    'checkout%5Bshipping_address%5D%5Baddress2%5D': '11',
    'checkout%5Bshipping_address%5D%5Bcity%5D': 'burnaby',
    'checkout%5Bshipping_address%5D%5Bcountry%5D': 'Canada',
    'checkout%5Bshipping_address%5D%5Bprovince%5D': 'British+Columbia',
    'checkout%5Bshipping_address%5D%5Bzip%5D': 'v5h0b7',
    'checkout%5Bshipping_address%5D%5Bphone%5D': '1+212-312-3122',
    'checkout%5Bremember_me%5D': '',
    'checkout%5Bremember_me%5D': '0',
    'button': '',
    'checkout%5Bclient_details%5D%5Bbrowser_width%5D': '243',
    'checkout%5Bclient_details%5D%5Bbrowser_height%5D': '660',
    'checkout%5Bclient_details%5D%5Bjavascript_enabled%5D': '1'
}


# In[145]:


response = s.post(shippingRequestUrl, data = postData, headers = header, allow_redirects=True)
print(response.status_code)
print(response.text)
print(response)


# In[148]:





# In[ ]:


a


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


ga = s.cookies.get_dict()


# In[ ]:


ga


# In[ ]:




