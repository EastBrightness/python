import cv2
import mediapipe as mp # 구글에서 제공해주는 영상모듈임.

# 비디오를 읽어줘
cap = cv2.VideoCapture('person.jpg')    # 0

mp_fd = mp.solutions.face_detection # 얼굴 찾는 애를 객체에 담은 것임.
mp_draw = mp.solutions.drawing_utils # 그려주는 애를 객체에 담은 것.
# 50% 이상의 얼굴이면, 얼굴로 인식해줘.
fd = mp_fd.FaceDetection(0.5) # 정확도 조정

# 읽은 비디오를 여러개의 이미지로 변경하라.
success, img = cap.read()
# 크기 조정
img = cv2.resize(img, (680, 960))
# 색보정 (정확도)
from_bgr_to_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# 얼굴을 찾아줘
result = fd.process(from_bgr_to_rgb)

# 얼굴을 찾으면
if result.detections:
    for id, detection in enumerate(result.detections):
        mp_draw.draw_detection(img, detection)  # 네모표시

# 보여줘
cv2.imshow('title', img)
# 기다려
cv2.waitKey(0)