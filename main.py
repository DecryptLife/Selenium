from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

barve_path = '/usr/bin/brave-browser'

options = Options()
options. binary_location = barve_path

browser = webdriver.Chrome(options=options)
browser.get('https://www.amazon.com/s?i=fashion-mens&bbn=23610279011&rh=n%3A7141123011%2Cn%3A23610279011%2Cn%3A7147441011%2Cn%3A1040658%2Cn%3A1045558&s=exact-aware-popularity-rank&ref=s9_bw_cg_SBPWINDT_4d1_w')

elem_list = browser.find_element(By.CSS_SELECTOR, "div.s-main-slot.s-result-list.s-search-results.sg-row")

items = elem_list.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')


for item in items:
    title = item.find_element(By.TAG_NAME, 'h2').text

    price = "No price provided"
    image =  "No image provided"

    link = item.find_element(By.CLASS_NAME, 'a-link-normal').get_attribute('href')
    try:
        price = item.find_element(By.CSS_SELECTOR, '.a-price').text.replace("\n",".")
    except: 
        pass


    try:
        image = item.find_element(By.CSS_SELECTOR,'.s-image').get_attribute("src")
    except:
        pass


    print("Title: "+title)
    print("Price: "+price)
    print("Image: "+image)
    print("LINK: "+link+"\n")