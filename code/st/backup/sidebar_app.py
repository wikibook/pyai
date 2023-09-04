# 사이드바 표시 사용 예제

import streamlit as st
from PIL import Image

# ---------- 사이드바 화면 구성 --------------------
st.sidebar.title("사이드바 ")
st.sidebar.header("텍스트 입력 사용 예")
user_id = st.sidebar.text_input('아이디(ID) 입력', value="streamlit", max_chars=15)
user_password = st.sidebar.text_input('패스워드(Password) 입력', value="abcd", type="password")

st.sidebar.header("셀렉트박스 사용 예")
selectbox_options = ['진주 귀걸이를 한 소녀', '별이 빛나는 밤', '절규', '월하정인'] # 셀렉트박스의 선택 항목
your_option = st.sidebar.selectbox('좋아하는 작품은?', selectbox_options, index=3) # 셀렉트박스의 항목 선택 결과
st.sidebar.write('**당신의 선택**:', your_option)

# ---------- 메인(Main) 화면 구성 --------------------
st.title("스트림릿의 사이드바 사용 예")

folder = 'C:/myPyAI/data/st/'

# selectbox_options의 요소에 따라서 보여줄 이미지 파일 리스트(selectbox_options의 요소와 순서를 일치시킴)
image_files = ['Vermeer.png', 'Gogh.png', 'Munch.png', 'ShinYoonbok.png'] # 이미지 파일 리스트

# 셀렉트박스에서 선택한 항목에 따라 이미지 표시
selectbox_options_index = selectbox_options.index(your_option) # selectbox_options의 리스트 인덱스 찾기
image_file = image_files[selectbox_options_index] # 선택한 항목에 맞는 이미지 파일 지정
image_local = Image.open(folder + image_file)     # Image.open() 함수로 이미지 파일 열기
st.image(image_local, caption=your_option)        # 이미지 표시
