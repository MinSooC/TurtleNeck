import time
import speech_recognition as sr

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

def speak_stop(duration):
    r = sr.Recognizer()
    checktime = time.time()
    timecheck = checktime

    while True:
        # 만약 중간에 잡음 등으로 마이크가 인식되었다면 except 구문 실행 후 다시 처음부터 시간을 재기 때문에, 지나간 시간만큼 영상길이에서 뺌
        timeout = duration - (timecheck - checktime)

        if timeout <= 0:
            break

        with sr.Microphone() as source:
            print('재생을 멈추시려면 이야기해주세요')
            try:
                # 영상이 재생되는 내내 인식하게끔 함
                audio = r.listen(source, timeout = timeout)
            except:
                print('영상이 끝났습니다.')
                break
        try:
            stopword = r.recognize_google(audio, language='ko-KR')
            print('음성 : ' + stopword)

            if '멈춰' in stopword or '그만' in stopword:
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

def run_videos(keyword):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.maximize_window()

    url = 'https://www.youtube.com/results?search_query={0}'.format(keyword)
    driver.get(url)
    time.sleep(8)  # 화면이 완전히 로딩될때까지 기다리기

    # 영상의 총 길이 구하기
    try:
        length = driver.find_element(By.XPATH, "//span[@class = 'style-scope ytd-thumbnail-overlay-time-status-renderer']")
        length_text = length.text
        minutes, seconds = map(int, length_text.split(':'))
        duration = minutes * 60 + seconds
        
    # 만약 로딩된 화면에 추출할 수 있는 영상 길이가 없을 때 (= 재생할 수 있는 영상이 없을때) PAGE_DOWN 키를 1회 입력
    except:
        body = driver.find_element(By.TAG_NAME, 'body')
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        length = driver.find_element(By.XPATH, "//span[@class = 'style-scope ytd-thumbnail-overlay-time-status-renderer']")
        length_text = length.text
        minutes, seconds = map(int, length_text.split(':'))
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

    stopword = speak_stop(duration - 3)
    # 만약 '멈춰'나 '그만'이 음성에 포함되어있다면 영상 재생 기능을 종료
    if '멈춰' in keyword or '그만' in stopword:
        driver.quit()
        return

    # 영상의 시간이 다 되면 크롬을 종료
    driver.quit()
