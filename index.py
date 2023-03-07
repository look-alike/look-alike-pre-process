from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import urllib.request
import os

keyword = input("검색할 유튜버 이름을 입력하세요: ")
number = int(input('검색할 개수를 입력하세요: '))

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get("https://www.google.co.kr/imghp?hl=ko")
elem = driver.find_element(By.NAME, "q")
elem.send_keys(keyword)
elem.send_keys(Keys.RETURN)
time.sleep(1)
images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")
count = 0
for image in images:
    try:
        image.click()
        time.sleep(2)
        imageUrl = driver.find_element(By.XPATH,"//*[@id='islrg]/div[1]/div[3]/a[1]/div[1]/img").get_attribute('src')
        urllib.request.urlretrieve(imageUrl, "imgfile/" + keyword + str(count) + ".jpg")
        print(f"Image saved: {count}")
        count += 1
        print(count, number)
        if (count == number):
            break
    except:
        pass
driver.close()