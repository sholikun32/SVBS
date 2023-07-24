import streamlit as st

def main():
    st.title("Login App")
    
    # Create username and password input fields
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    # Check if the login button is pressed
    if st.button("Login"):
        if authenticate(username, password):
            st.success("Login successful!")
        else:
            st.error("Invalid username or password.")

def authenticate(username, password):
    # You can customize this function to validate the credentials.
    # For simplicity, I'll just hardcode a valid username and password.
    valid_username = "admin"
    valid_password = "password"
    
    if username == valid_username and password == valid_password:
        return True
    else:
        return False

if __name__ == "__main__":
    main()
