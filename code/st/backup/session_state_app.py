# 세션 상태 사용 예제

import streamlit as st

st.title("세션 상태 사용 예")

# 세션 상태 초기화
if 'count' not in st.session_state: # st.session_state에 'count'가 없으면
    st.session_state['count'] = 0    # st.session_state['count']를 0으로 초기화

if 'registered' not in st.session_state: # st.session_state에 'registered'가 없으면
    st.session_state['registered'] = []   # st.session_state['registered']를 빈 리스트로 초기화
    
# 텍스트 입력 위젯    
user_input = st.text_input('이름', value="이름을 입력하세요.", key='name')

# 버튼 입력 위젯
clicked = st.button('등록')

if clicked: # 버튼 입력을 클릭하면
    st.session_state['count'] = st.session_state['count'] + 1 # 1씩 증가
    st.write("버튼 입력 회수:", st.session_state['count']) # 버튼 입력 회수 화면에 표시
    
    name = st.session_state['name'] # st.session_state.name도 동일 
    st.session_state['registered'].append(name) # 리스트에 입력한 이름 추가
    st.write("등록 이름 리스트:", st.session_state['registered']) # 리스트 내용 화면에 표시
