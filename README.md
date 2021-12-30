# toyproject_snow

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
