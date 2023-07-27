import streamlit as st
import streamlit.components.v1 as components

def login_page():
    st.markdown("""
    <style>
    .login-container {
        padding: 2rem;
        max-width: 400px;
        margin: auto;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        border-radius: 8px;
        background-color: #f9f9f9;
    }
    .input-field {
        margin-bottom: 1rem;
    }
    .login-btn {
        background-color: #007BFF;
        color: white;
        padding: 0.5rem 1rem;
        border: none;
        border-radius: 4px;
        cursor: pointer;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 style="text-align:center;">Modern Login</h1>', unsafe_allow_html=True)

    # Login Form
    with st.form(key='login-form', class_='login-container'):
        username = st.text_input('Username', key='username', class_='input-field')
        password = st.text_input('Password', key='password', class_='input-field', type='password')
        login_button = st.form_submit_button('Login', class_='login-btn')

    # Handle login functionality here
    if login_button:
        # Validate username and password
        if username == 'your_username' and password == 'your_password':
            st.success('Login successful!')
        else:
            st.error('Invalid credentials')

