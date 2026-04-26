import streamlit as st

users = {
    "2024603039": "23683512!jin",
    "admin": "admin"
}

def login():
    if "login" not in st.session_state:
        st.session_state.login = False

    if not st.session_state.login:
        st.markdown("## 🔐 로그인")

        col1, col2 = st.columns(2)

        with col1:
            user = st.text_input("아이디")

        with col2:
            pw = st.text_input("비밀번호", type="password")

        if st.button("로그인"):
            if user in users and users[user] == pw:
                st.session_state.login = True
                st.success("로그인 성공")
                st.rerun()
            else:
                st.error("로그인 실패")

    return st.session_state.login