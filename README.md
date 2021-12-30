# toyproject_snow

### 프로젝트 개요
- 얼굴인식 스노우 카메라처럼 흉내내서 만들기 (opencv, dlib 사용)


![result_image](https://user-images.githubusercontent.com/84002580/147728127-afaaf352-05c3-4493-a30b-256b032fe089.jpg)



### 파일 설명
- main.py 파이썬 실행 파일
- overlay_pre.py 인식한 얼굴에 다른 이미지를 덮어씌우는 함수 정의
- face_landmark.dat 68개 얼굴 특징점을 추출하기 위해 기존 학습된 데이터파일
- smaples 폴더 : 동영상(girl.mp4), 얼굴에 덮어씌울 이미지(ryan_transparent.png)

### 진행 순서
#### 1. python 가상 환경 만들기
- anaconda prompt 실행
- conda create -n dlib python=3.6
- conda activate dlib
#### 2. cv2, dlib 라이브러리 설치
- conda install opencv-python
- conda install -c conda-forge dlib
- 참고: https://blog.naver.com/PostView.nhn?blogId=os2dr&logNo=221818707061&categoryNo=0&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView
#### 3. 실행
- command or terminal에서 python main.py

#### * 주의할 점
- dlib 설치가 쉽지 않았으나, conda 가상환경에서 conda install...로 하는 법이 가장 무난하였음
- python 3.x 버전에서 dlib 설치가 가능하다는 말이 있어서 3.x 버전 사용 (다른 버전은 test 안했음)

#### 출처: https://blog.naver.com/dnjswns2280/221882217386
(original) https://opentutorials.org/module/3811/22895
