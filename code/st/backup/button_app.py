# 기본 버튼 입력 예제

import streamlit as st

st.title("스트림릿의 버튼 입력 사용 예")

clicked = st.button('버튼 1')
st.write('버튼 1 클릭 상태:', clicked)

if clicked:
     st.write('버튼 1을 클릭했습니다.' )
else:
     st.write('버튼 1을 클릭하지 않았습니다.' )
        
clicked = st.button('버튼 2')
st.write('버튼 2 클릭 상태:', clicked)

if clicked:
     st.write('버튼 2를 클릭했습니다.' )
else:
     st.write('버튼 2를 클릭하지 않았습니다.' )
