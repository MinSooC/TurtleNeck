# 📂 프로젝트명
### ✅ 인공지능 비서 거북이 (메타버스 아카데미 7월 월말 프로젝트)

# 📒 프로젝트 소개
### ✅ Mediapipe와 CNN을 활용한 거북목 탐지와 Speech-Recognition을 통한 AI스피커를 개발하는 프로젝트입니다.

주제선정 배경은 다음과 같습니다.

><img src="https://github.com/MinSooC/TurtleNeck/blob/main/tools/assets/%EA%B1%B0%EB%B6%81%EB%AA%A9%20%ED%99%98%EC%9E%90%20%EC%88%98.png?raw=true" height="360">

>> 국민관심질병통계(일자목ㆍ거북목), 건강보험심사평가원

컴퓨터를 이용하는 대부분의 사람들은 작업하면서 한번쯤은 스트레칭을 한 경험이 있을 것입니다. 

건강보험심사평가원에서 조사한 국민관심질병통계에 따르면 거북목 문제로 내원하는 환자들은 표에 나와있듯 매년 220만명 언저리입니다. 저희는 따로 병원에 방문하지 않는 거북목 환자들을 포함한다면 그 수는 저희가 예상할 수 없을 정도로 훨씬 많아지리라 예상했습니다.

그래서 저희는 컴퓨터 이용 중 거북목 탐지라는 주제를 바탕으로 프로그램을 개발하고자 했고, 거북목만 탐지할 뿐 아니라 생활 전반에 도움이 될 수 있는 인공지능 스피커를 개발하고자 하였습니다.
<br>
<br>

# 👩‍🔧 팀원 소개 및 역할
### ✅ 팀원
메타버스 아카데미 2기 AI-B반 김종민, 오수종, 차민수 (3명)

### ✅ 역할 분담
 - 주제 선정 : 모든 팀원
 - 거북목 데이터 수집 : 김종민
 - 거북목 탐지 구현(정면) : 오수종
 - 거북목 탐지 구현(측면) : 김종민
 - 인공지능 스피커 구현 : 차민수
 - 발표 PPT 제작 : 차민수
 - 발표 및 시연 : 모든 팀원
<br>

# 📅 프로젝트 진행 기록
### ✅ 수행 기간 : 2023.07.13 ~ 2023.07.21
### ✅ 세부 진행 기록
 - 2023.07.13 ~ 2023.07.16 : 프로젝트 주제 탐색 
 - 2023.07.17 : 프로젝트 주제 최종 결정, 인공지능 스피커 구현
 - 2023.07.18 : 인공지능 스피커 구현
 - 2023.07.19 : 인공지능 스피커 구현, 코드 합치기(1)
 - 2023.07.20 : 인공지능 스피커 구현, 코드 합치기(2), PPT 초안 제작
 - 2023.07.21 : 인공지능 스피커 구현, 최종 PPT 제출 및 과제 제출<br>
 ++
 - 2023.07.31 : 최종 PPT 발표
<br>

# 📜 주요기능
### ✅ 음성인식 및 Text-To-Speech
1. Speech-Recognition 패키지 / gTTS 패키지 사용
2. 마이크 기능 on / off를 함수를 통해 구현(마이크가 한 기능에 중복해서 켜져있지 않도록)
3. tts로는 안내기능을 출력


### ✅ 타이머 설정
1. 정면 거북목 인식 : Mediapipe
2. 측면 거북목 인식 : CNN

<br>
이하 기능들은 전부 Selenium Web Driver 사용

### ✅ 음악재생
1. Melon의 Top100 순위를 crop해서 youtube 음원으로 자동으로 재생
2. 음악 재생 중 중단 후 다음 음악, 혹은 아예 음악재생 기능 종료 기능 포함


### ✅ 영상재생
1. 인식된 keyword를 Youtube 검색어로 집어넣음
2. 광고 등을 클릭하지 않기 위해 만약 한 페이지 전체가 광고로 가득찼다면 자동으로 스크롤 다운
3. 영상 재생 중 기능 종료 기능 포함


### ✅ 키워드 검색
1. 인식된 keyword를 구글 검색창에다 입력


### ✅ 뉴스 검색
1. 인식된 keyword를 바탕으로 해당 주제의 Naver 뉴스 홈페이지를 띄움
2. 연예 / 스포츠 뉴스 검색 가능


### ✅ 지도 검색
1. 인식된 keyword를 google map에 넣어 출력


### ✅ 날씨 알리미
1. 오늘 / 내일 날씨를 해당 장소 기반으로 알려줌 (Google 날씨 기반)
2. 기본적으로 날짜(오늘/내일), 장소, 날씨, 기온을 알려주고, 만약 날씨가 비나 소나기이면 강수확률도 같이 출력



# 🛠 기술 스택

### 🔹 언어
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">

### 🔹 주요 라이브러리
<img src="https://img.shields.io/badge/selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white"> <img src="https://img.shields.io/badge/tensorflow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white"> <img src="https://img.shields.io/badge/pytorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white"> <img src="https://img.shields.io/badge/torchvision-29A7DF?style=for-the-badge&logo=torchvision&logoColor=white"> <img src="https://img.shields.io/badge/opencv-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white"> <img src="https://img.shields.io/badge/MediaPipe-1299F3?style=for-the-badge&logo=MediaPipe&logoColor=white"> <img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"> <img src="https://img.shields.io/badge/numpy-013243?style=for-the-badge&logo=numpy&logoColor=white"> <img src="https://img.shields.io/badge/matplotlib-0058CC?style=for-the-badge&logo=matplotlib&logoColor=white"> <img src="https://img.shields.io/badge/Speech%20recognition-512BD4?style=for-the-badge&logoColor=white"> <img src="https://img.shields.io/badge/Playsound-F9AB00?style=for-the-badge&logoColor=white"> <img src="https://img.shields.io/badge/Text to Speech-40AEF0?style=for-the-badge&logoColor=white">

### 🔹 개발 툴
<img src="https://img.shields.io/badge/pycharm-000000?style=for-the-badge&logo=pycharm&logoColor=white"> <img src="https://img.shields.io/badge/Google Colab-F9AB00?style=for-the-badge&logo=Google Colab&logoColor=white">
