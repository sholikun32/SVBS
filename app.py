from os import path
import streamlit as st
import streamlit.components.v1 as com

# Set wide layout
st.set_page_config(
    page_title='SVBS',
    page_icon='✅',
    layout='wide'
)

# Secret username and password (replace with your actual values)
SECRET_USERNAME = "admin"
SECRET_PASSWORD = "password"

# Initialize session state
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# Login header
st.markdown("""
<h1 style='text-align:center;padding: 0px 0px;color:Orange;font-size:400%;'>SVBS</h1>
<h2 style='text-align:center;padding: 0px 0px;color:Black;font-size:150%;'>SmartViz BPJS System</h2>
""", unsafe_allow_html=True)

# Login form
if not st.session_state.authenticated:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username == SECRET_USERNAME and password == SECRET_PASSWORD:
            st.session_state.authenticated = True
        else:
            st.error("Invalid username or password. Please try again.")

# Display content after successful login
if st.session_state.authenticated:
    com.html("""
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <html>
        <body>
        <div class='tableauPlaceholder' id='viz1693260760119' style='position: relative'>
            <noscript><a href='#'><img alt='HOME ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Bo&#47;Book1j_16894983558260&#47;HOME&#47;1_rss.png' style='border: none' /></a></noscript>
            <object class='tableauViz'  style='display:none;'>
                <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
                <param name='embed_code_version' value='3' />
                <param name='site_root' value='' />
                <param name='name' value='Book1j_16894983558260&#47;HOME' />
                <param name='tabs' value='no' />
                <param name='toolbar' value='yes' />
                <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Bo&#47;Book1j_16894983558260&#47;HOME&#47;1.png' />
                <param name='animate_transition' value='yes' />
                <param name='display_static_image' value='yes' />
                <param name='display_spinner' value='yes' />
                <param name='display_overlay' value='yes' />
                <param name='display_count' value='yes' />
                <param name='language' value='en-US' />
                <param name='filter' value='publish=yes' />
            </object>
        </div>
        <script type='text/javascript'>
            var divElement = document.getElementById('viz1693260760119');
            var vizElement = divElement.getElementsByTagName('object')[0];
            if ( divElement.offsetWidth > 800 ) {
                vizElement.style.width='1650px';
                vizElement.style.height='1627px';
            } else if ( divElement.offsetWidth > 500 ) {
                vizElement.style.width='1650px';
                vizElement.style.height='1627px';
            } else {
                vizElement.style.width='100%';
                vizElement.style.height='727px';
            }
            var scriptElement = document.createElement('script');
            scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
            vizElement.parentNode.insertBefore(scriptElement, vizElement);
        </script>
        </body>
        </html>
        """, height=4600)
