from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request
import os
import sys

search = input("검색어: ")  # 이미지 이름
count = int(input("download counts: "))   # 크롤링할 이미지 개수
# "crawled_images/" # 이미지들을 저장할 폴더 주소
folder = "crawled_images/"  + search + '_' + str(count)
folder_name = search + '_' + str(count)

# 중복되는 폴더 명이 없다면 생성
if not os.path.exists(folder):
    os.makedirs(folder)
# 중복된다면 문구 출력 후 프로그램 종료
else:
    print('이전에 같은 [검색어, 이미지 수]로 다운로드한 폴더가 존재합니다.')
    sys.exit(0)

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=ri&ogbl")
elem = driver.find_element(By.NAME, "q")
elem.send_keys(search)
elem.send_keys(Keys.RETURN)

#스크롤 내리는거
SCROLL_PAUSE_TIME = 1

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_elements(By.CSS_SELECTOR, ".mye4qd").click()
        except:
            break
            
    last_height = new_height

#스크롤 다 내림

images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")

for i in range(count):
    try:
        images[i].click()
        time.sleep(1) 
        imgUrl = driver.find_element(By.XPATH,
            '//*[@id="Sva75c"]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]').get_attribute("src")
        # driver.find_elements_by_css_selector(".n3VNCb").get_attribute("src")
        urllib.request.urlretrieve(imgUrl, "crawled_images/" + folder_name + "/" + search + '_' + str(i) + ".jpg")
    except:
        pass


driver.close()
