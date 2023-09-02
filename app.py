from os import path, listdir
import streamlit as st
import streamlit.components.v1 as com
import warnings

# Ignore warning
warnings.simplefilter(action='ignore', category=FutureWarning)

# Set wide layout
st.set_page_config(
    page_title='SVBS',
    page_icon='✅',
    layout='wide'
)

# Define the correct username and password (you can store these securely)
correct_username = "your_username"
correct_password = "your_password"

st.markdown("""
<h1 style='text-align:center;padding: 0px 0px;color:Orange;font-size:400%;'>SVBS</h1>
<h2 style='text-align:center;padding: 0px 0px;color:Black;font-size:150%;'>SmartViz BPJS System</h2>
""", unsafe_allow_html=True)

def main():
    if st.session_state.logged_in:
        # User is logged in, display the content
        display_dashboard()
    else:
        # User is not logged in, display the login form
        display_login()

def display_login():
    st.header("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username == correct_username and password == correct_password:
            # Set session state to indicate that the user is logged in
            st.session_state.logged_in = True
        else:
            st.error("Invalid username or password")

def display_dashboard():
    com.html("""
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <html>
        <body>
        <div class='tableauPlaceholder' id='viz1693260760119' style='position: relative'><noscript><a href='#'><img alt='HOME ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Bo&#47;Book1j_16894983558260&#47;HOME&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Book1j_16894983558260&#47;HOME' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Bo&#47;Book1j_16894983558260&#47;HOME&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>
        <script type='text/javascript'>var divElement = document.getElementById('viz1693260760119');var vizElement = divElement.getElementsByTagName('object')[0];if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1650px';vizElement.style.height='1627px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1650px';vizElement.style.height='1627px';} else { vizElement.style.width='100%';vizElement.style.height='727px';} var scriptElement = document.createElement('script');scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';vizElement.parentNode.insertBefore(scriptElement, vizElement);</script></body>
        </html>
        """
        , height=4600)

if __name__ == "__main__":
    main()
