# Selenium

### 1. Opening BRAVE from python code

- choose webdriver - requires further installation for some WebDrivers (Chrome, Firefox, Edge , etc)
- store the webdriver to a browser => browser = webdriver.WEB_DRIVER_NAME
- to open => browser.get(link)

### Fetching elements from websites

This part we are fetching information from [amazon website](https://www.amazon.com/s?i=fashion-mens&bbn=23610279011&rh=n%3A7141123011%2Cn%3A23610279011%2Cn%3A7147441011%2Cn%3A1040658%2Cn%3A1045558&s=exact-aware-popularity-rank&ref=s9_bw_cg_SBPWINDT_4d1_w)

Displaying each item's title,price, image and product link

- using find_elements(By.PARAMETERS(CSS_SELECTOR, XPATH, TAG_NAME and more)) we can target specific items on the page
- once we get all the items and store it we can traverse the list and use the above function to target specific parts of the item
- when we need something other than text use get_attribute("PARAMETER") to get that particular value
- use try and catch so as to avoid interruption in case certain values are missing
