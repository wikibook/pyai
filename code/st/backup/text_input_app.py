# 텍스트 입력의 사용 예제

import streamlit as st

st.title("스트림릿의 텍스트 입력 사용 예")

user_id = st.text_input('아이디(ID) 입력', value="streamlit", max_chars=15)
user_password = st.text_input('패스워드(Password) 입력', value="abcd", type="password")

if user_id == "streamlit":
    if user_password == "1234":
        st.write('로그인됐습니다. 서비스를 이용할 수 있습니다.')
    else:
        st.write('잘못된 패스워드입니다. 다시 입력하세요.')
else:
    st.write('없는 ID입니다. 회원 가입을 하거나 올바른 ID를 입력하세요.')
