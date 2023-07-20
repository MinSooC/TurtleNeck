import time
import speech_recognition as sr

import requests
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup


def speak_stop(duration):
    r = sr.Recognizer()
    checktime = time.time()
    timecheck = checktime

    while True:
        timeout = duration - (timecheck - checktime)

        if timeout <= 0:
            break

        with sr.Microphone() as source:
            print('재생을 멈추시려면 이야기해주세요')
            try:
                audio = r.listen(source, timeout = timeout)
            except:
                print('음악이 끝났습니다.')
                return '다음'

        try:
            stopword = r.recognize_google(audio, language='ko-KR')
            print('음성 : ' + stopword)

            if '멈춰' in stopword or '그만' in stopword:
                return stopword
            elif '다음' in stopword:
                return stopword
            else:
                timecheck = time.time()
                pass

        except sr.UnknownValueError:
            print('음성을 다시 입력해주세요')
            timecheck = time.time()

        except:
            print('알 수 없는 오류가 발생했습니다.')
            timecheck = time.time()


def play_music():
    html = requests.get('https://www.melon.com/chart/index.htm', headers={'User-Agent': 'Mozilla/5.0'}).text
    bs = BeautifulSoup(html, 'html.parser')
    result = bs.find_all('div', class_='ellipsis rank01')

    keywords = []
    for temp in result:
        keywords.append(temp.find('a').text)

    for keyword in keywords:
        while True:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_experimental_option('detach', True)
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
            driver.maximize_window()
            url = 'https://www.youtube.com/results?search_query={0}'.format(keyword + ' 음원')
            driver.get(url)
            time.sleep(8)  # 화면이 완전히 로딩될때까지 대기하기

            # 영상의 총 길이 구하기
            try:
                length = driver.find_element(By.XPATH, "//span[@class = 'style-scope ytd-thumbnail-overlay-time-status-renderer']")
                length_text = length.text
                minutes, seconds = map(int, length_text.split(':'))
                
                # 보통 유튜브로 노래 이름 + 음원으로 검색하면 나오는 영상의 길이는 10분 안팎이기에 영상의 길이가 20분이 넘으면 광고로 판단한다.
                if minutes > 20:
                    raise

                break

            except:
                driver.quit()  # 만약 광고 등의 이유로 영상 길이를 구하는데 있어 오류가 발생시 크롬 창을 닫고 다시 검색
                pass

        duration = minutes * 60 + seconds

        # 유튜브의 첫 영상의 썸네일을 클릭하는 코드
        driver.find_element(By.XPATH, '//*[@id="thumbnail"]/yt-image/img').click()
        time.sleep(2)
        print(keyword, '을/를 재생합니다.', '길이:', str(minutes) + '분', str(seconds) + '초')

        # ↓ 키를 n번 입력시켜주는 코드 : 기본설정인 음량 100에서 ↓키 1회 입력마다 5씩 줄어듦
        actions = ActionChains(driver)
        for _ in range(10):
            actions.send_keys(Keys.ARROW_DOWN)
        actions.perform()

        # 광고 건너뛰기를 눌러주는 코드
        for _ in range(2):
            try:
                time.sleep(8)
                driver.find_element(By.CSS_SELECTOR, ".ytp-ad-text.ytp-ad-skip-button-text").click()
            except:
                pass

        stopword = speak_stop(duration - 4)
        # 만약 '멈춰'나 '그만'이 음성에 포함되어있다면 노래 재생 기능을 아예 종료, 만약 '다음'이 음성에 포함되어있다면 다음 음악으로 진행
        if '멈춰' in stopword or '그만' in stopword:
            driver.quit()
            return
        else:
            pass

        driver.quit()
