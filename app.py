from os import path, listdir
import streamlit as st
from streamlit_embedcode import github_gist
import streamlit.components.v1 as com

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import streamlit.components.v1 as components
import streamlit.components.v1 as stc



# Ignore warning
st.set_option('deprecation.showPyplotGlobalUse', False)
# Set wide layout
st.set_page_config(
    page_title = 'SVBS',
    page_icon = '✅',
    layout = 'wide'
)

 
st.markdown("""
<h1 style='text-align:center;padding: 0px 0px;color:Orange;font-size:400%;'>SVBS</h1>
<h2 style='text-align:center;padding: 0px 0px;color:Black;font-size:150%;'>SmartViz BPJS System</h2>

""", unsafe_allow_html=True)

def check_password():
    """Returns `True` if the user had a correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if (
            st.session_state["username"] in st.secrets["passwords"]
            and st.session_state["password"]
            == st.secrets["passwords"][st.session_state["username"]]
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store username + password
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show inputs for username + password.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input("Password", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input("Password", type="password", on_change=password_entered, key="password")
        st.error("😕 Tekan enter untuk username dan password")
        return False
    else:
        # Password correct.
        return True

if check_password():
    com.html("""
           <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <html>
            <body>
          <div class='tableauPlaceholder' id='viz1694837311886' style='position: relative'><noscript><a href='#'><img alt='HOME ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Bo&#47;Book1j_16894983558260&#47;HOME&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Book1j_16894983558260&#47;HOME' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Bo&#47;Book1j_16894983558260&#47;HOME&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1694837311886');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1670px';vizElement.style.height='2297px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1670px';vizElement.style.height='2297px';} else { vizElement.style.width='100%';vizElement.style.height='827px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>  </body>
            </html>
            """, height=6000)
