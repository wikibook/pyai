# 오디오 재생 예제

import streamlit as st

st.title("스트림릿의 오디오 재생 예")

# 1) 컴퓨터 내에 있는 오디오 파일을 열어서 재생
st.subheader("1. 컴퓨터 내의 오디오 파일을 재생")

audio_file = 'C:/myPyAI/data/st/서연의_하루_TTS_배경음악_short.mp3' # 오디오 파일 경로
audio_local = open(audio_file, 'rb')
audio_bytes = audio_local.read()

st.text("MP3 파일. format='audio/mpeg'")
st.audio(audio_bytes, format='audio/mpeg')

# 2) 웹상에 있는 오디오 파일의 주소(URL)를 이용해 오디오 재생
st.subheader("2. 웹상에 있는 오디오를 재생")

audio_url1 = "https://samplelib.com/lib/preview/wav/sample-15s.wav" # 오디오 URL
st.text("Wave 파일. format='audio/wav'")
st.audio(audio_url1, format='audio/wav') # st.audio(audio_url1) 도 동일

audio_url2 = "https://cdn.pixabay.com/download/audio/2022/10/14/audio_9939f792cb.mp3"
st.text("MP3 파일. format='audio/mpeg'")
st.audio(audio_url2, format='audio/mpeg')

audio_url3 = "https://freetestdata.com/wp-content/uploads/2021/09/Free_Test_Data_1MB_OGG.ogg"
st.text("OGG 파일. format='audio/ogg'")
st.audio(audio_url3, format='audio/ogg')
