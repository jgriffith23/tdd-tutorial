from selenium import webdriver

browser = webdriver.Chrome("/Users/jennifer/Downloads/chromedriver")
browser.get("http://localhost:8000")

assert "Django" in browser.title

