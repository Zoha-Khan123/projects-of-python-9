import streamlit as st
import re
import math
import random

def check_password_strength(password):
    score = 0
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        st.write("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]" , password) and re.search(r"[a-z]", password):
        score += 1
    else:
        st.write("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        st.write("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        st.write("❌ Include at least one special character (!@#$%^&*).")
    
    # Strength Rating
    if score == 4:
        st.write("✅ Strong Password!")
    elif score == 3:
        st.write("⚠️ Moderate Password - Consider adding more security features.")
    else:
       st.write("❌ Weak Password - Improve it using the suggestions above.")

# Header
st.title("Password Strength Checker 🔒")
st.write("Check the strength of your password and get suggestions to make it stronger.")

# Generate Random Password
option = ["Pq7$kL@3","X9yT$2Lm","A1@kFp%3","Z2fL@p7T","mL9$Xq1K"]
choose = math.floor(random.random()*len(option))
random_password = option[choose]

# Input field for password
password = st.text_input("Enter your password:",type="password")

# Button to check password strength
if st.button("Check Password Strength"):
    if password:
        check_password_strength(password)
    else:
        st.write("---")
        st.write("💡 Need a strong password? Try this one:")
        st.success(random_password)




