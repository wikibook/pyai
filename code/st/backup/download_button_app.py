# 다운로드 버튼 사용 예제

import streamlit as st
import pandas as pd
from io import BytesIO

# 스트림릿 화면 구성
st.title("스트림릿의 다운로드 버튼 사용 예")

st.subheader("텍스트 파일 다운로드 예제")

folder = 'C:/myPyAI/data/st/'

with open(folder + "서연의_이야기.txt", encoding='utf-8') as text_file:
    text_data = text_file.read()
    st.download_button(
            label="텍스트 파일 다운로드", 
            data = text_data, 
            file_name="서연의_이야기.txt"
    )

st.subheader("이미지 파일 다운로드 예제")

with open(folder + "sample_image.png",'rb') as image_file:
    st.download_button(
            label="이미지 파일 다운로드",
            data=image_file,
            file_name="sample_image.png",
            mime="image/png"
    )
    
st.subheader("오디오 파일 다운로드 예제")

with open(folder + "서연의_하루_TTS_배경음악_short.mp3",'rb') as audio_file:
    st.download_button(
            label="오디오 파일 다운로드",
            data=audio_file,
            file_name="서연의_하루_TTS_배경음악_short.mp3",
            mime="audio/mpeg"
    )
