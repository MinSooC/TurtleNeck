import time

import speech_recognition as sr
from gtts import gTTS
import playsound

import get_musics
import get_videos
import search_google
import weather

import face_detection
import winsound as sd

def get_tts(text, filename):
    tts = gTTS(text=text, lang='ko')                                # 변수 tts에 gTTS 코드를 저장, 음성 타입은 한국어
    tts.save('mp3/' + filename)                                     # 변수 tts를 filename으로 저장 (fimename의 파일 형식은 .mp3)로 filename 대입시 꼭 붙일것
    time.sleep(1.5)                                                 # 저장시간을 고려한 대기시간 설정

def speak(r):
    while True:
        with sr.Microphone() as source:
            print('원하시는 기능을 말해주세요')
            playsound.playsound('mp3/please_talk.mp3')
            audio = r.listen(source, timeout=10)                   # 만약 timeout = 10초 간 음성의 입력이 없다면, WaitTimeoutError 예외 발생

        try:
            keyword = r.recognize_google(audio, language='ko-KR')  # 음성을 구글 음성인식을 통해 text로 만듦
            print('음성 : ' + keyword)
            return keyword                                         # 만약 음성을 인식했다면 구글 음성인식을 통해 text로 변환되어 저장된 keyword 변수를 리턴

        except sr.UnknownValueError:
            print('음성을 다시 입력해주세요')

        except:
            print('알 수 없는 오류가 발생했습니다.')

def speak_video(r):
    while True:
        with sr.Microphone() as source:
            print('이제 검색어를 입력해주세요')
            audio = r.listen(source, timeout=10)

        try:
            word = r.recognize_google(audio, language='ko-KR')
            print('음성 : ' + word)
            return word

        except sr.UnknownValueError:
            print('음성을 다시 입력해주세요')

        except:
            print('알 수 없는 오류가 발생했습니다.')

def beepsound():
    fr = 5225
    du = 500
    sd.Beep(fr, du)

def get_valid_time():
    while True:
        try:
            hours = int(input('시간을 숫자로 입력해주세요(0-23): '))
            minutes = int(input('분을 숫자로만 입력해주세요(0-59): '))
            if hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
                raise ValueError('올바르게 입력되지 않았습니다.')

            return (hours, minutes)

        except ValueError as e:
            print(e)
            print('다시 입력해주세요.')

        except:
            print('다시 입력해주세요.')


text = '안녕하세요 인공지능 비서입니다.'
print(text)
# get_tts(text, 'welcome_secretary.mp3')                           # 만약 해당 파일을 실행한 폴더에 'welcome.secretary.mp3' 파일이 있다면 주석 처리. 이는 앞으로 나올 모든 get_tts 함수에 해당
playsound.playsound('mp3/welcome_secretary.mp3')

text = '원하시는 기능을 말해주세요.'
# get_tts(text, 'please_talk.mp3')

r = sr.Recognizer()

while True:
    keyword = speak(r)

    if ('음악' in keyword or '노래' in keyword) and '틀어' in keyword:
        text = '음악을 검색합니다.'
        print(text)
        # get_tts(text, 'music_search.mp3')
        playsound.playsound('mp3/music_search.mp3')
        get_musics.play_music()

    elif '영상' in keyword and '틀어' in keyword:
        text = '동영상을 검색합니다. 검색어를 입력해주세요.'
        print(text)
        # get_tts(text, 'video_search.mp3')
        playsound.playsound('mp3/video_search.mp3')

        word = speak_video(r)
        print(word + '(이)란 주제로 유튜브 검색을 시작합니다.')
        get_videos.run_videos(word)

    elif 'Google' in keyword or '검색' in keyword:
        text = '검색어를 입력해주세요.'
        print(text)
        # get_tts(text, 'search.mp3')
        playsound.playsound('mp3/search.mp3')

        word = speak_video(r)
        print(word + '(이)란 주제로 구글 검색을 시작합니다.')
        search_google.google_search(word)

    elif '타이머' in keyword:
        text = '타이머를 실행합니다.'
        print(text)
        # get_tts(text, 'timer.mp3')
        playsound.playsound('mp3/timer.mp3')

        while True:
            (hours, minutes) = get_valid_time()
            print('타이머를 실행합니다. 실행시간:', str(hours) + '시간', str(minutes) + '분')
            timer = hours * 60 * 60 + minutes * 60
            
            if timer == 0:
                beepsound()
                print('0시간 0분은 불가능합니다. 다시 입력해주세요.')
            else:
                break

        face_detection.face_detect()

    elif '오늘' in keyword and '날씨' in keyword:
        weather.weather_today()

    elif '종료' in keyword or '끝' in keyword:
        break

text = '인공지능 비서가 종료됩니다. 이용해주셔서 감사합니다.'
print(text)
# get_tts(text, 'byebye.mp3')
playsound.playsound('mp3/byebye.mp3')