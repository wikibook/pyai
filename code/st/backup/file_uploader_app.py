# 파일 업로더 사용 예제

import streamlit as st
from io import StringIO

st.title("스트림릿의 파일 업로더 사용 예")

uploaded_file = st.file_uploader("Text 파일을 선택하세요.", type='txt')
if uploaded_file is not None:    
    # 텍스트 파일을 읽어서 문자열로 변환
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    string_data = stringio.read()
    st.write(string_data[:100]) # 일부의 내용 출력
    
uploaded_file = st.file_uploader("MP3 파일을 선택하세요.", type='mp3')
if uploaded_file is not None:
    # 바이너리 파일을 읽어서 바이트로 변환
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data[:100]) # 일부의 내용 출력
