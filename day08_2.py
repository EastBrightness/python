import cv2

# pip install python-opencv
# pip install opencv-python

def ShowImage(img_path):
    # 이미지 읽어줘
    img = cv2.imread('person.jpg')
    # 이미지 보여줘
    cv2.imshow('title', img)
    # 무한대기
    cv2.waitKey(0)

def ShowVideo(video_path):
    # 동영상 읽어줘
    vc = cv2.VideoCapture(video_path)
    # 무한반복 ( 동영상 == 빠르게 여러 이미지를 출력하는 것임.)
    while True:   
        # 읽기성공여부, 동영상을 자른 이미지
        success, img = vc.read()
        # 동영상을 성공적으로 읽었으면
        if success:
            cv2.imshow('title', img)
        if cv2.waitKey(1) & 0xFF == 27: # 27 : ESC를 의미함. c언어에서 배움
            # 동영상 waitKey 20~25를 주면서 가장 적절한 거에 맞춤.
            break 

def ShowCam():
    # 캠 읽어줘
    vc = cv2.VideoCapture(0) # 파라미터가 0이면, 캠을 읽음
    # 화면 조정
    vc.set(3, 640)  # 3 : 가로
    vc.set(4, 480)  # 4 : 세로

    # 무한반복 ( 동영상 == 빠르게 여러 이미지를 출력하는 것임.)
    while True:   
        # 읽기성공여부, 동영상을 자른 이미지
        success, img = vc.read()
        # 동영상을 성공적으로 읽었으면
        if success:
            cv2.imshow('title', img)
        if cv2.waitKey(1) & 0xFF == 27: # 27 : ESC를 의미함. c언어에서 배움
            # 캠 : waitKey 를 1로 줌.
            break 


# ShowImage('person.jpg')
# ShowVideo('person.mp4')
ShowCam()