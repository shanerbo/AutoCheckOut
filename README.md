# YSAutoCheck

# Use it at your own risk. It may or may not work.

This is a personal project. 

Two recommended approaches:

1. Use selenium to autofill all the informations. Selenium will track changes in website. If the taget product is up, selenium will send a message via WeChat.

2. Send http requests and form info using requests. Browser is not required. Since it is hard to get Googla Analyst cookie, we needs to open a browser once to get cookie. Then browser will send post requests for adding product, filling out shipping info and credit card info.

TODO: Hype products require CAPTCHA. As per my investigation, once a CAPTCHA is passed, it will generate a cookie and no more CAPTCHA will show up.

