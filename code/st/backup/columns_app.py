# 세로 단(컬럼) 분할 사용 예제

import streamlit as st
from PIL import Image

st.title("스트림릿에서 화면 분할 사용 예")

# 1) 2개로 세로 단 분할 (예제 1)
[col1, col2] = st.columns(2) # 너비가 같은 2개의 세로 단으로 구성
with col1: # 첫 번째 세로 단(컬럼)
    st.subheader("유튜브 비디오1")
    url_col1 = "https://www.youtube.com/watch?v=bagb1zxqMTg"
    st.video(url_col1)

with col2: # 두 번째 세로 단(컬럼)
    st.subheader("유튜브 비디오2")
    url_col2 = "https://www.youtube.com/watch?v=i-E7NiyRDa0"
    st.video(url_col2)

# 2) 3개로 세로 단 분할 (예제 2)
columns = st.columns([1.1, 1.0, 0.9]) # 너비가 다른 3개의 세로 단으로 구성

folder = 'C:/myPyAI/data/st/'                    # 폴더 지정
image_files = ['dog.png', 'cat.png', 'bird.png'] # 이미지 파일명 리스트
image_cations = ['강아지', '고양이', '새']       # 이미지 캡션 리스트

for k in range(len(columns)):
    with columns[k]: # 세로 단(컬럼) 지정
        st.subheader(image_cations[k])                    # 세로 단별로 subheader 표시
        image_local = Image.open(folder + image_files[k]) # 세로 단별로 이미지 열기
        st.image(image_local,caption=image_cations[k])    # 세로 단별로 이미지 표시
