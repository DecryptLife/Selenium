from selenium import webdriver
from selenium.webdriver.chrome.options import Options

barve_path = '/usr/bin/brave-browser'

options = Options()
options. binary_location = barve_path

browser = webdriver.Chrome(options=options)
browser.get('http://selenium.dev/')