import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

from gtts import gTTS
import playsound

def weather_days(keyword):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.maximize_window()

    if '오늘' in keyword:
        day_word = '오늘'
    elif '내일' in keyword:
        day_word = '내일'

    url = "https://www.google.com/search?q="+ day_word +"날씨&sxsrf=AB5stBhWE2Kpz033hjTMs3lLOk9XuXntdQ%3A1689819319624&ei=t5i4ZLfUJevM1e8P9Y2fgAk&ved=0ahUKEwj3i5_Cm5yAAxVrZvUHHfXGB5AQ4dUDCA8&uact=5&oq=%EC%98%A4%EB%8A%98+%EB%82%A0%EC%94%A8&gs_lp=Egxnd3Mtd2l6LXNlcnAiDeyYpOuKmCDrgqDslKgyBhAAGAcYHjIGEAAYBxgeMgYQABgHGB4yBhAAGAcYHjIGEAAYBxgeMgYQABgHGB4yBhAAGAcYHjIGEAAYBxgeMgUQABiABDIGEAAYBxgeSMgMUNkHWMULcAJ4AZABAZgBhQGgAeIEqgEDMC41uAEDyAEA-AEBwgIKEAAYRxjWBBiwA-IDBBgAIEGIBgGQBgo&sclient=gws-wiz-serp"
    driver.get(url)
    time.sleep(1.5)

    place_element = driver.find_element(By.XPATH, "//span[@class = 'BBwThe']")
    place = place_element.text

    tem_element = driver.find_element(By.XPATH, "//span[@class = 'wob_t q8U8x']")
    temperature = tem_element.text

    wea_element = driver.find_element(By.XPATH, "//span[@id = 'wob_dc']")
    weather = wea_element.text

    if '동반' in weather:
        weather = '천둥, 번개를 동반한 많은 비'
    elif '광역성 뇌우' in weather:
        weather = '천둥, 번개를 동반한 비'
    elif '광역성 소나기' in weather:
        weather = '소나기'
    else:
        pass

    rain_element = driver.find_element(By.XPATH, "//span[@id = 'wob_pp']")
    rain = rain_element.text

    if '소나기' in weather or '비' in weather:
        text = f'{day_word} {place}의 날씨는 {weather}이며, 기온은 {temperature}도 입니다. 강수 확률은 {rain}입니다.'
        print(text)
    else:
        text = f'{day_word} {place}의 날씨는 {weather}이며, 기온은 {temperature}도 입니다.'
        print(text)

    tts = gTTS(text = text, lang= 'ko')
    tts.save('mp3/weather_predict.mp3')
    time.sleep(1.5)
    playsound.playsound('mp3/weather_predict.mp3')

    # 함수를 연속으로 호출했을 때 발생하는 파일 접근 문제 해결
    time.sleep(0.5)
    os.remove("./mp3/weather_predict.mp3")
