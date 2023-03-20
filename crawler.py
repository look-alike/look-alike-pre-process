from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import urllib.request
import ssl
import os

# ssl certification 오류 해결
ssl._create_default_https_context = ssl._create_unverified_context

keyword = input("검색할 이름을 입력하세요: ")

# 파일명 영어로 변경
keyword_to_english = ''
if keyword == "송혜교": 
  keyword_to_english = 'shg'
elif keyword == "이도현":
  keyword_to_english = 'idh'
elif keyword == '임지연':
  keyword_to_english = 'ijh'
elif keyword == '신예은':
  keyword_to_english = 'she'
elif keyword == '손명오':
  keyword_to_english = 'smo'

# selenium option
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# 저장할 디렉토리명
save_path = '/Users/jang-youngjoon/dev-projects/youtuber-look-alike/crawled-image'

# 제일 아래까지 스크롤 -> 항목 높이기
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

# 더보기 버튼 누르는 코드
selenium_scroll_option()

images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")
count = 1
images_url_list = []
for image in images:
  if image:
    # image.send_keys(Keys.ENTER) #.click() 말고 send_keys(Keys.ENTER)로 변경
    driver.execute_script("arguments[0].click();", image)
    time.sleep(3)
    imageUrl = driver.find_element(By.XPATH,'//*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div[1]/div[2]/div[2]/div/a/img')
    if imageUrl:
      if (imageUrl.get_attribute('src') == None):
        images_url_list.append(imageUrl.get_attribute('data-src'))
      else:
        images_url_list.append(imageUrl.get_attribute('src'))
    else:
      continue
  else:
    break

for image_url in images_url_list:
  file_name = keyword_to_english + '_' + str(count) + ".jpg"
  file_place = os.path.join(save_path, file_name)
  urllib.request.urlretrieve(image_url, file_place)
  print(f"Image saved: {count}")
  count += 1
driver.close()




