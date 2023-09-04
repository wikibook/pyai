# 콜백 함수 사용 예제

import streamlit as st

st.title("콜백 함수 사용 예")

# 세션 상태 초기화
if 'lang' not in st.session_state:    # st.session_state에 'lang'이 없으면
    st.session_state['lang'] = '영어'  # st.session_state['lang']를 '영어'로 초기화

# 콜백 함수    
def button_callback(sel_lang): 
    st.session_state['lang'] = sel_lang
        
# 라디오 버튼        
radio_options = ['영어', '프랑스어', '독일어']
radio_selected = st.radio('한국어를 어떤 언어로 번역하겠습니까?', radio_options)

# 기본 버튼: on_click에 콜백 함수(button_callback)를 지정, args에 콜백 함수 인수 지정 
clicked = st.button('선택', on_click=button_callback, args=[radio_selected])

# 콤백 함수를 실행한 결과를 출력
st.write(f"한국어를 {st.session_state['lang']}로 번역하는 것을 선택했습니다.")
