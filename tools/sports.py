from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def find_sports(keyword):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.maximize_window()

    if keyword == '한국 야구' or keyword == '야구':
        sports = 'kbaseball'
    elif keyword == '해외 야구':
        sports = 'wbaseball'
    elif keyword == '한국 축구' or keyword == '축구':
        sports = 'kfootball'
    elif keyword == '해외 축구':
        sports = 'wfootball'
    elif keyword == '농구':
        sports = 'basketball'
    elif keyword == '배구':
        sports = 'volleyball'
    elif keyword == '골프':
        sports = 'golf'
    else:
        sports = 'general'

    url = 'https://sports.news.naver.com/' + sports + '/index'
    driver.get(url)
