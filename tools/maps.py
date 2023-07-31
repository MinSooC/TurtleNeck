import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def map_search(keyword):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager(version="114.0.5735.90").install()), options=chrome_options)
    driver.maximize_window()

    # 구글 지도의 검색창에 keyword를 넣어서 검색 실시
    url = "https://www.google.co.kr/maps/"
    driver.get(url)

    time.sleep(2)
    driver.find_element(By.ID, 'searchboxinput').send_keys(keyword)  # 검색어를 구글 지도의 검색창에 집어넣음
    driver.find_element(By.ID, 'searchbox-searchbutton').click()  # 검색 버튼을 클릭
