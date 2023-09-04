# 비디오 재생 예제

import streamlit as st

st.title("스트림릿의 비디오 재생 예")

# 1) 컴퓨터에 있는 비디오 파일을 열어서 재생
st.subheader("1. 컴퓨터에 있는 비디오 파일을 재생")

st.text("앞에서 살펴본 오디오 재생 방법과 유사")

# video_file = 'C:/myPyAI/data/st/sample_video.mp4' # 비디오 파일 경로
# video_local = open(video_file ,'rb')
# video_bytes = video_local.read()

# st.text("MP4 파일. format='video/mp4'") 
# st.video(video_bytes, format='video/mp4') # st.video(video_bytes) 도 동일

# 2) 유튜브 비디오 주소(URL)를 이용해 비디오 재생
st.subheader("2. 유튜브 비디오를 재생")

video_url = "https://www.youtube.com/watch?v=5VxYrmnwQiA" # 유튜브 비디오 URL
st.text("MP4 파일. format='video/mp4'")
st.video(video_url, format='video/mp4') # st.video(video_url) 도 동일
