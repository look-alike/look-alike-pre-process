from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

keyword = input("검색할 유튜버 이름을 입력하세요: ")
# number = int(input('검색할 개수를 입력하세요: '))

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# 더보기 버튼 누르는 코드
# selenium_scroll_option()
# driver.find_element(By.XPATH,'//*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div[1]/div[2]/div[2]/div/a/img')[0].click()
# selenium_scroll_option()

def selenium_scroll_option():
  SCROLL_PAUSE_SEC = 2
  last_height = driver.execute_script("return document.body.scrollHeight")

  while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(SCROLL_PAUSE_SEC)
    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:
      break;
    last_height = new_height

driver.get("https://www.google.co.kr/imghp?hl=ko")
elem = driver.find_element(By.NAME, "q")
elem.send_keys(keyword)
elem.send_keys(Keys.RETURN)
time.sleep(1)
images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")
count = 0
images_url_list = []
for image in images:
  image.click()
  time.sleep(2)
  imageUrl = driver.find_element(By.XPATH,'//*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div[1]/div[2]/div[2]/div/a/img')
  if (imageUrl.get_attribute('src') == None):
    images_url_list.append(imageUrl.get_attribute('data-src'))
  else:
    images_url_list.append(imageUrl.get_attribute('src'))

for image_url in images_url_list:
  urllib.request.urlretrieve(image_url, "imgfile" + '_' + keyword + '_' + str(count) + ".jpg")
  print(f"Image saved: {count}")
  count += 1
  # print(count, number)
  # if (count == number):
  #     break;
driver.close()




