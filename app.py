
import streamlit as st
from database import init_db
from auth import register_user, login_user

st.set_page_config(page_title='PolyMatch', layout='wide')
init_db()

st.markdown('<h1 style="text-align:center;color:#2563EB;">🎓 PolyMatch</h1>', unsafe_allow_html=True)
st.markdown('<h3 style="text-align:center;">AI Powered Polytechnic Placement Portal</h3>', unsafe_allow_html=True)

menu = st.sidebar.selectbox('Menu', ['Home','Register','Login'])

if menu == 'Home':
    st.success('Welcome to PolyMatch')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric('Students', '1,200+')
    with col2:
        st.metric('Companies', '150+')
    with col3:
        st.metric('Placements', '850+')

elif menu == 'Register':
    st.subheader('Create Account')
    name = st.text_input('Full Name')
    email = st.text_input('Email')
    password = st.text_input('Password', type='password')
    role = st.selectbox('Role', ['student','employer'])

    if st.button('Register'):
        ok, msg = register_user(name, email, password, role)
        if ok:
            st.success(msg)
        else:
            st.error(msg)

elif menu == 'Login':
    st.subheader('Login')
    email = st.text_input('Email')
    password = st.text_input('Password', type='password')

    if st.button('Login'):
        user = login_user(email, password)
        if user:
            st.session_state.user = user
            st.success(f"Welcome {user['name']}")
        else:
            st.error('Invalid credentials')
