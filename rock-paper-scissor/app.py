import streamlit as st
import random
import math

projects_name = ["Rock ✋ Paper ✌️ Scissor","Number Guessing Game"]

selected_project = st.sidebar.radio("Select a Project", projects_name)

if selected_project == "Rock ✋ Paper ✌️ Scissor":
    st.title("Python Project 4")
    st.header("✊ Rock ✋ Paper ✌️ Scissor Game")

    # User Choice
    user_choice =st.selectbox("Select an option" , ("Rock", "Paper", "Scissor") , index=None , placeholder="👇 Select an option")

    #Computer Choice
    options = ["Rock","Paper","Scissor"]
    random_choice = math.floor(random.random()*len(options))
    computer_choice = options[random_choice]


    #Result
    if st.button("🔥 Start Game 🔥"):
        st.write(f"You Choose: {user_choice}")
        st.write(f"Computer Choose: {computer_choice}")
        # Conditions
        if (user_choice == "Rock" and computer_choice == "Scissor" or user_choice == "Paper" and computer_choice == "Rock" or user_choice == "Scissor" and computer_choice == "Paper"):
            st.success("🎉 YOU WIN! 🎉")
        elif (user_choice == computer_choice):
            st.warning("🤝 IT'S A TIE!")
        else:
            st.error("💔 YOU LOSE! Better luck next time.")


# =========================== Number Guessing Game =========================
if selected_project == "Number Guessing Game":
    st.title("Number Guessing Game")