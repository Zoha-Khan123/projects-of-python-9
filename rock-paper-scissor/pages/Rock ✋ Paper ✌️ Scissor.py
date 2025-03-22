import streamlit as st
import random
import math

# Set page configuration
st.set_page_config(page_title="Rock Paper Scissor Game", page_icon="✊")

# Title
st.title("✊ :rainbow[Rock] ✋ :rainbow[Paper] ✌️ :rainbow[Scissor Game]")

# Display Instructions in a Container
with st.container(border=True):
    st.title("📝 :red[Instructions]")
    st.write("""
    1. **Objective**: Beat the computer in a game of Rock, Paper, Scissors.
    2. **How to Play**:
       - Select your choice (Rock, Paper, or Scissor) from the dropdown menu.
       - Click the **"Start Game"** button to play.
    3. **Rules**:
       - **Rock** beats **Scissor**.
       - **Paper** beats **Rock**.
       - **Scissor** beats **Paper**.
       - If both players choose the same option, it's a tie.
    4. **Result**: The game will display whether you won, lost, or tied.
    """)

# =========================== Rock Paper Scissor =========================
st.title(":rainbow[Start Your Game]")

# User Choice
user_choice =st.selectbox("👇 Select an option" , ("Rock", "Paper", "Scissor") , index=None , placeholder="Select an option")

#Computer Choice
options = ["Rock","Paper","Scissor"]
random_choice = math.floor(random.random()*len(options))
computer_choice = options[random_choice]


#Result
if st.button("🔥 Play 🔥"):
    if(user_choice == None):
        st.warning("Please choose some option")
    else:
        st.write(f"You Choose: {user_choice}")
        st.write(f"Computer Choose: {computer_choice}")
        # Conditions
        if (user_choice == "Rock" and computer_choice == "Scissor" or user_choice == "Paper" and computer_choice == "Rock" or user_choice == "Scissor" and computer_choice == "Paper"):
            st.success("🎉 YOU WIN! 🎉")
            st.balloons()
        elif (user_choice == computer_choice):
            st.warning("🤝 IT'S A TIE!")
        else:
            st.error("💔 YOU LOSE! Better luck next time.")

