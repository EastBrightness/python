# import가 안되는 이유 : 설치가 안된 라이브러리(모듈) 또는 오타
# 외부 모듈 설치 : pip install 모듈명

# pip install opencv-python
import cv2

이미지 = cv2.imread('img1.png')     # 이미지를 읽어줘.
cv2.imshow('title', 이미지)         # 보여줘

cv2.waitKey(0)                      # 무한대기

cv_img('../img/tokki.png')          # ../ : 뒤로가기 후, /img 폴더로 들어가서 찾기.
