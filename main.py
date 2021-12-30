import cv2
import dlib
import numpy as np
import sys
from overlay_pre import overlay_processing

# 동영상 크기를 조절해 줄 변수
scaler = 0.3
# 얼굴 디텍터 모듈 초기화
detector = dlib.get_frontal_face_detector()
# 68개의 얼굴 특징점 추출
predictor = dlib.shape_predictor('face_landmark.dat')
# load video
cap = cv2.VideoCapture('./samples/girl.mp4')

# load overlay image
overlay = cv2.imread('samples/ryan_transparent.png', cv2.IMREAD_UNCHANGED)


while True:
    ret, img = cap.read()
    print(ret)
    if not ret:
        break
    # 이미지 크기 조절
    img = cv2.resize(img, (int(img.shape[1]*scaler), int(img.shape[0]*scaler)))
    ori = img.copy()
    # 얼굴 인식
    faces = detector(img)
    # 여러 얼굴이 나오기 때문에 얼굴 한개만 지정
    face = faces[0]
    # 얼굴 특징점 추출
    dlib_shape = predictor(img, face)
    shape_2d = np.array([[p.x, p.y] for p in dlib_shape.parts()])
    # compute center and boundaries of face / 얼굴 중심을 구함
    top_left = np.min(shape_2d, axis=0)
    botton_right = np.max(shape_2d, axis=0)
    # 덥어씌울 이미지 크기
    face_size = int(max(botton_right - top_left) * 1.8)
    center_x, center_y = np.mean(shape_2d, axis=0).astype(np.int)
    # center_x, y 값을 조정하여 덮어씌울 이미지 center 조정
    result = overlay_processing.overlay_transparent(
        ori, overlay, center_x+25, center_y-25, overlay_size=(face_size, face_size))

    #visualize / 시각화
    img = cv2.rectangle(img, pt1=(face.left(), face.top()), pt2=(face.right(), face.bottom()), color=(255, 255, 255),
                        thickness=2, lineType=cv2.LINE_AA)
    # 얼굴 특징점 68개 점찍기
    for s in shape_2d:
        cv2.circle(img, center=tuple(s), radius=1, color=(
            255, 255, 255), thickness=2, lineType=cv2.LINE_AA)
    # top_left, bottom_right 파란 점찍기
    cv2.circle(img, center=tuple(top_left), radius=1, color=(
        255, 0, 0), thickness=2, lineType=cv2.LINE_AA)
    cv2.circle(img, center=tuple(bottom_right), radius=1,
       color=(255, 0, 0), thickness=2, lineType=cv2.LINE_AA)
    # center 빨간 점찍기
    cv2.circle(img, center=tuple((center_x, center_y)), radius=1,
           color=(0, 0, 255), thickness=2, lineType=cv2.LINE_AA)
    
    # 비디오 출력하기
    cv2.imshow('ori', ori)
    cv2.imshow('img', img)
    cv2.imshow('result', result)
    cv2.waitKey(1)
