import streamlit as st

col1, col2 = st.columns([2,3])
tab1, tab2 = st.tabs(['Tab A', 'Tab B'])
with col1 :
    st.title("here is column1 title")
    with tab1 :
        st.write('존재하는 이유 그런건 아무래도 좋으니 그리 즐겁지도 괴롭지도 않은 바람아 불어라 달을 찾는 이유 예쁜 건 언제봐도 좋으니 나는 세계의 시계를 부수고 너에게 닿는다')
    with tab2 :
        st.write("hi")

with col2 :
    st.title("here is column2 title")
    st.checkbox("this is checkbox1 in col2 ")

col1.subheader("I am column1 subheader")
col2.checkbox("this is checkbox2 in col2")