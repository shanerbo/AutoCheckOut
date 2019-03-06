# YSAutoCheck


Personal insterests, may or may not work.

Two approaches:

1. Using selenium to autofill all the info, it will track if there is change in website. If the taget product is up, it will send message via WeChat.

2. Send http requests and form info using requests, no need to open broswer. Since its hard to get Googla Analyst(_ga) cookie, it needs to open a browser once to get that cookie, after that it will send post requests for adding product, filling out shipping info and credit card info.

TODO: For hype product, it requires CAPTCHA. As my investigation, once you pass a CAPTCHA, it will generates a cookie so that you will not need to pass CAPTCHA.

# Use it at your own risk.
