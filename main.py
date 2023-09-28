from selenium import webdriver
from selenium.webdriver.chrome.service import Service
s = Service("C:\\Users\\vika_\\PycharmProjects\\test\\chromedriver\\chromedriver.exe")
import time


url = "https://vk.com/"
browser = webdriver.Chrome(service=s)


try:
    browser.get(url=url)
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    browser.close()
    browser.quit()