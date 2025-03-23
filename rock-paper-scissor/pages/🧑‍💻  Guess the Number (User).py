import streamlit as st
import random

# Set page configuration
st.set_page_config(page_title="Guess the Number (User)", page_icon="🧑‍💻")

st.title("🧑‍💻:rainbow[Guess the Number (User)]")


# Display Instructions in a Container
with st.container(border=True):
    st.title("📝 :red[Instructions]")
    st.write("""
    1. **Objective**: Think of a number between 1 and 100, and let the computer guess it.
    2. **How to Play**: 
       - The computer will show a guess.
       - Click "Too Low" if your number is higher, "Too High" if it's lower, or "Correct!" if it’s right.
    3. **Feedback**: 
       - The computer adjusts its guess based on your input.
       - The range narrows with each guess.
    4. **Reset the Game**: Click "Reset Game" to start over with a new number.
    5. **Attempts Counter**: See how many guesses the computer takes in the Attempts section.
    """)

def guess_the_number():
    if "low" not in st.session_state:
        st.session_state.low = 1
    if "high" not in st.session_state:
        st.session_state.high = 100 
    if "guess" not in st.session_state:
        st.session_state.guess = random.randint(st.session_state.low,st.session_state.high)
    if "guess_count" not in st.session_state:
        st.session_state.guess_count = 0    


    st.title(":rainbow[Start Your Game]")
    st.write("Welcome to the Guess the Number Game! The computer will try to guess your number between 1 and 100.", divider="green")
    st.write("Is this your number?")
    st.title(f":rainbow[{st.session_state.guess}]")


    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Low", use_container_width=True):
            st.session_state.guess_count += 1
            st.session_state.low = st.session_state.guess + 1
            if st.session_state.low <= st.session_state.high:
                st.session_state.guess = random.randint(st.session_state.low,st.session_state.high)
                st.rerun()

    with col2:
        if st.button("High", use_container_width=True):
            st.session_state.guess_count += 1
            st.session_state.high = st.session_state.guess - 1
            if st.session_state.low <= st.session_state.high:
                st.session_state.guess = random.randint(st.session_state.low,st.session_state.high)
                st.rerun()

    with col3:
        correct_clicked = st.button("Correct!", use_container_width=True)
            
    if correct_clicked:
        st.success(f"Yayyyyyy! Computer guessed your number in {st.session_state.guess_count} attempts!", icon="🎉")
        st.balloons()


    # Attempts Counter
    with st.container(border=True):
        st.title(":rainbow[Attempts]")
        st.write(f"**Attempts:** {st.session_state.guess_count}")
    st.divider()

    if st.button("Reset the Game", key="reset_button", use_container_width=True):
                st.session_state.guessing_the_number_random = random.randint(1, 100)
                st.session_state.guess_count = 0
                st.rerun()

if __name__ == "__main__":
    guess_the_number()