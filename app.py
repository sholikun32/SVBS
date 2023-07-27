import streamlit as st
import streamlit.components.v1 as components

# Custom CSS for the login page
custom_css = """
<style>
/* Add your custom CSS styles here */
body {
  background-color: #f4f4f4;
}

.login-container {
  max-width: 400px;
  margin: 100px auto;
  padding: 20px;
  border-radius: 10px;
  background-color: #ffffff;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
}

.login-header {
  text-align: center;
  font-size: 24px;
  margin-bottom: 20px;
}

.login-input {
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
  border: 1px solid #cccccc;
  border-radius: 5px;
}

.login-button {
  width: 100%;
  padding: 10px;
  background-color: #007bff;
  color: #ffffff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.login-button:hover {
  background-color: #0056b3;
}

</style>
"""

# Custom HTML for the login form
login_form = """
<div class="login-container">
  <div class="login-header">Login</div>
  <input class="login-input" type="text" placeholder="Username">
  <input class="login-input" type="password" placeholder="Password">
  <button class="login-button">Log in</button>
</div>
"""

def main():
    st.title("Modern Streamlit Login")

    # Inject custom CSS into the Streamlit app
    components.html(custom_css)

    # Inject the login form into the Streamlit app
    components.html(login_form)

if __name__ == "__main__":
    main()
