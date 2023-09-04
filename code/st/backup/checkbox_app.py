# 체크박스 사용 예제

import streamlit as st

st.title("스트림릿의 체크박스 사용 예")

checked1 = st.checkbox('체크박스 1')
st.write('체크박스 1 상태:', checked1)
       
if checked1:
     st.write('체크박스 1을 체크했습니다.' )
else:
     st.write('체크박스 1을 체크하지 않았습니다.' )
        
checked2 = st.checkbox('체크 박스 2', value=True)
st.write('체크박스 2 상태:', checked2)

if checked2:
     st.write('체크박스 2를 체크했습니다.' )
else:
     st.write('체크박스 2를 체크하지 않았습니다.' )
