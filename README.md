# YSAutoCheck


This is a personal project. It may or may not work.

Two approaches recommended:

1. Use selenium to autofill all the info. It will track changes in website. If the taget product is up, it will send a message via WeChat.

2. Send http requests and form info using requests. Broswer is not needed. Since its hard to get Googla Analyst(_ga) cookie, it needs to open a browser once to get that cookie. Then it will send post requests for adding product, filling out shipping info and credit card info.

TODO: Hype products require CAPTCHA. As per my investigation, once a CAPTCHA is passed, it will generates a cookie so that no more CAPTCHA will show up.

# Use it at your own risk.
