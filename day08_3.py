import cv2
import mediapipe as mp # 구글에서 제공해주는 영상모듈임.

# pip install mediapipe

# 만약에 OS 권한문제로 설치가 안될경우, 
'''
0. 파이썬 실행중인지 체크한다 (실행중일떄는 다운로드가 안된다.)
1. anaconda prompt를 관리자 권한으로 실행
2. python -m pip install --upgrade pip 를 입력해서 pip를 업그레이드 시켜줌
'''

'''
만약에 웹캠이면 VideoCapture에 0을 넣고, 맨 밑 WaitKey에 1을 넣는다.
'''
# 드래그 + Shift + Tab : 전체 땡겨오기

cap = cv2.VideoCapture('person.mp4')    # 0
mp_fd = mp.solutions.face_detection # 얼굴 찾는 애를 객체에 담은 것임.
mp_draw = mp.solutions.drawing_utils # 그려주는 애를 객체에 담은 것.
fd = mp_fd.FaceDetection(1) # 파라미터 변경을 통해 정확도 조정이 가능함. 기본값은 0.5

# 무한반복 ( 동영상 == 빠르게 여러 이미지를 출력하는 것임.)
while True:   
    # 읽기성공여부, 동영상을 자른 이미지
    success, img = cap.read()
    # 동영상을 성공적으로 읽었으면, 보여주기 전에 얼굴을 찾는다.
    if success:
        from_bgr_to_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 얼굴찾기 정확도 향상을 위해 BGR -> RGB
        face = fd.process(from_bgr_to_rgb)  # 얼굴 찾기

        if face.detections: # 얼굴을 찾으면,
            # 얼굴을 찾았다! ==> 사람 얼굴을 찾은 다음 하고 싶은 동작
            # 함수 사용하기
            for id, detection in enumerate(face.detections): # enumerate : 리스트에 순번을 매겨 튜플로 만드는 친구
                # mp_draw.draw_detection(img, detection)  # mediapipe - 기본적인 얼굴을 사각형 표시
                # print(detection)  # 정보 표시해줌. 
                # print(detection.location_data.relative_bounding_box)
                fd_box = detection.location_data.relative_bounding_box
                box = int(fd_box.xmin * img.shape[1]), int(fd_box.ymin * img.shape[0]), \
                    int(fd_box.width * img.shape[1]), int(fd_box.height * img.shape[0])
                cv2.rectangle(img, box, (0,0,255), 2) # img에 box를 그릴건데, 이 색으로, 이 두꼐

                cv2.putText(img, f'정확도 : {round(detection.score[0]*100, 1)}%', (box[0], box[1]), cv2.FONT_ITALIC, 2, (0, 0, 0), 2)

                # print(box)
                # print(img.shape) img의 shape

        cv2.imshow('title', img)
    if cv2.waitKey(1) & 0xFF == 27: # 27 : ESC를 의미함. c언어에서 배움
        # 캠 : waitKey 를 1로 줌.6
        break 

img = cv2.imread('person.jpg')
cv2.imshow('title', img)
cv2.waitKey(0)