import cv2
import torch
import numpy as np
import winsound as sd

from PIL import ImageFont,ImageDraw,Image
from torchvision import datasets, models, transforms

# 비프음 함수
def beepsound():
    fr = 300    # range : 37 ~ 32767
    du = 200     # 1000 ms ==1second
    sd.Beep(fr, du)


def side_detect(timer):
    # 0: 거묵복자세, 1:바른 자세
    class_name = ['bent posture', 'upright posture']

    # 캠 열기
    vcap = cv2.VideoCapture(0) #기본카메라 열기

    # 영상에서 들어온 이미지를 변환하기 (리사이즈, tensor로 타입변경, 노멀라이즈)
    transform_test = transforms.Compose([
        transforms.Resize(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=(0.4914,0.4822,0.4465),std=(0.247,0.243,0.261))
    ])

    # 모델(파라미터 및 구성저장됨) 불러오기
    model = torch.load('./models/model_All.pth')
    model.eval()

    # 자세 저장 리스트
    pose_list = ['upright posture']

    # 프레임 기준숫자
    nums = 0
    second = 0

    while True:
        ret, frame = vcap.read()

        if not ret:
            break

        # 현재 자세출력과 리스트에 저장하기위한 기준숫자설정
        nums += 1

        # inference 작업
        # 캠에서 나온 이미지를 모델 추론용으로 따로 복사
        frame2 = frame.copy()

        # 이미지를 Image로 변환
        frame2 = Image.fromarray(np.uint8(frame2))

        # 224로 리사이즈
        frame2 = frame2.resize((224, 224))

        # 이미지를 transform하기
        frame2 = transform_test(frame2)

        # 0번 인덱스에 차원 추가
        frame2 = torch.unsqueeze(frame2, 0)

        # 모델의 예측값 불러오기
        preds = model(frame2)

        # 최종 예측값
        pred = torch.max(preds, 1)[1]

        # 예측값의 이름
        pose_name = class_name[pred[0]]

        # 예측값들을 30프레임마다(1초)마다 출력 자세저장리스트에 저장
        if nums % 30 == 0:
            # 타이머시간 줄이기
            timer -= 1
            # 자세저장리스트에 자세저장
            pose_list.append(pose_name)


            # 20초간격으로 측정하고 두번연속 거북목자세일시 사진저장
            if len(pose_list) >= 20 and pose_list[-1] == 'bent posture' and pose_list[-20] == 'bent posture':
                frame3 = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
                frame3 = Image.fromarray(frame3)
                frame3.save(f'./side data/{nums // 30}초.jpg')
                beepsound()
                # print(pose_name)
                # print(pose_list)

        # 화면에 예측값 표시하기
        cv2.putText(frame, f'Test {nums//30} {pose_list[-1]}', (50, 50), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255))
        # print(type(frame))

        cv2.imshow('cam',frame)

        if cv2.waitKey(1) == 27 or timer == 0:
            ## 거북목 리포트
            # 기능 정지시 그동안의 거북목자세시간 퍼센트 출력
            print('실행시간동안의 리포트')
            print(f'총 실행시간: {nums//30}초')
            print(f"거북목시간: {pose_list.count('bent posture')}초")
            break

    vcap.release()
    cv2.destroyAllWindows()

''' 전체 파일 실행이 필요없고 모델의 추론만 필요할시 코드

import cv2
import torch
import numpy as np
from PIL import ImageFont,ImageDraw,Image
from torchvision import datasets, models, transforms

# 영상에서 들어온 이미지를 변환하기 위한 코드 (리사이즈, tensor로 타입변경, 노멀라이즈)
transform_test = transforms.Compose([
    transforms.Resize(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=(0.4914,0.4822,0.4465),std=(0.247,0.243,0.261))
])

# 모델(파라미터 및 구성저장됨) 불러오기
model = torch.load('./model_All.pth')
model.eval()

# 캠에서 나온 이미지를 모델 추론용으로 따로 복사
frame2 = frame.copy()

# 이미지를 Image로 변환
frame2 = Image.fromarray(np.uint8(frame2))

# 224로 리사이즈
frame2 = frame2.resize((224, 224))

# 이미지 transform
frame2 = transform_test(frame2)

# 차원 추가
frame2 = torch.unsqueeze(frame2, 0)

# 모델의 예측값 불러오기
preds = model(frame2)

# 최종 예측값
pred = torch.max(preds, 1)[1]

# 예측값의 이름 (0, 1)
return pred[0]
'''