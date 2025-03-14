import streamlit as st
import re

# Check password strength
def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password length should be at least 8 characters"
    if not any(char.isdigit() for char in password):
        return "Weak: Password should have at least one numeral"
    if not any(char.isupper() for char in password):
        return "Weak: Password should have at least one uppercase letter"
    if not any(char.islower() for char in password):
        return "Weak: Password should have at least one lowercase letter"
    if not any(char in ['$', '#', '@', '&', '%'] for char in password):
        return "Weak: Password should have at least one of the symbols $, #, @, &, %"
    
    return "Strong: Your Password is Secure!"

# Streamlit UI
st.title("🔐 Password Strength Checker")

password = st.text_input("Enter your password:", type="password")

if st.button("Check Strength"):
    if password:
        result = check_password_strength(password)
        st.write(result)
    else:
        st.write("⚠️ Please enter a password.")
