<p align="center">
    <a href="https://dashboard.smartproxy.com/?page=residential-proxies&utm_source=socialorganic&utm_medium=social&utm_campaign=resi_trial_GITHUB"><img src="https://i.imgur.com/3uZgYJ9.png"></a>
</p>

## Dependencies

```http
BeautifulSoup
webdriver_manager
selenium
extension >> extension.py
```

## Authentication

You can create, edit, and delete proxy users in our Dashboard > Residential > Proxy setup page.

## Zalando Selenium Scraper

This code is a script in Python that uses the selenium and BeautifulSoup libraries to scrape product information from Zalando.

The script uses the Chrome web browser, controlled by the selenium library, to navigate to the website and retrieve its source code. The source code is then parsed using BeautifulSoup to extract specific information about each product on the page.

In order to use a proxy, the code uses the "webdriver_manager" and "extension" libraries to install the chrome driver and configure the Chrome browser to use a proxy server. The credentials for the proxy server, username, password, endpoint, and port are passed as arguments to the "proxies" function from the "extension" library (extension.py).

The script then uses BeautifulSoup to search the page source for specific tags containing the product information. The product information is then stored in a dictionary and added to a list "data".

Finally, the script saves the "data" list to a JSON file named "data.json".

