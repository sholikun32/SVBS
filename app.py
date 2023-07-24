import streamlit as st
from streamlit_bokeh_events import streamlit_bokeh_events

def main():
    st.set_page_config(
        page_title="Streamlit Bootstrap Example",
        layout="wide"
    )
    st.title("Streamlit Bootstrap Example")

    # Add your Streamlit app content here
    st.write("Welcome to the Streamlit Bootstrap Example!")
    
    # Create a Bootstrap-styled button
    st.button("Click me", key="click_button", help="A Bootstrap-styled button")

    # Use streamlit_bokeh_events to listen to button clicks
    result = streamlit_bokeh_events(
        events="click_button",
        key="listen_button",
        debounce_time=0,
        override_height=75,
        refresh_on_update=False,
        override_width=200,
    )

    if result:
        if "click_button" in result:
            st.write("Button clicked!")

if __name__ == "__main__":
    main()
