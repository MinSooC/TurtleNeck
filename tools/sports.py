from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def find_sports(keyword):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager(version="114.0.5735.90").install()), options=chrome_options)
    driver.maximize_window()

    # 스포츠 종목 별 검색, 야구와 축구의 경우 국내/해외 구분을 말하지 않으면 국내 야구/축구로 연결되도록 함
    if '한국 야구' in keyword or keyword == '야구':
        sports = 'kbaseball'
    elif '해외 야구' in keyword:
        sports = 'wbaseball'
    elif '한국 축구' in keyword or keyword == '축구':
        sports = 'kfootball'
    elif '해외 축구' in keyword:
        sports = 'wfootball'
    elif '농구' in keyword:
        sports = 'basketball'
    elif '배구' in keyword:
        sports = 'volleyball'
    elif '골프' in keyword:
        sports = 'golf'
    else:
        sports = 'general'

    url = 'https://sports.news.naver.com/' + sports + '/index'
    driver.get(url)
