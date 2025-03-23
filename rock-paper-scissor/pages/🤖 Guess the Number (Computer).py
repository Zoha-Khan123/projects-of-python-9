import streamlit as st
import random

# Set page configuration
st.set_page_config(page_title="Guess the Number (Computer)", page_icon="🤖")

st.title("🤖 :rainbow[Guess the Number (Computer)]")

# Display Instructions in a Container
with st.container(border=True):
    st.title("📝 :red[Instructions]")
    st.write("""
    1. **Objective**: Guess the secret number between 1 and 100.
    2. **How to Play**: Enter your guess in the input box and click the "Guess" button.
    3. **Feedback**:
       - If your guess is too low, the game will tell you to try a higher number.
       - If your guess is too high, the game will tell you to try a lower number.
       - If your guess is correct, you win!
    4. **Reset the Game**: Click the "Reset" button to start a new game.
    5. **Attempts Counter**: The number of attempts is displayed in the Attempts section.
    """)

def guess_the_number():
    st.title(":rainbow[Start Your Game]")
    st.write("Welcome to the Guess the Number Game! Try to guess the number between 1 and 100.", divider="green")

    # State for Guessing Number
    if "guessing_the_number_random" not in st.session_state:
        st.session_state.guessing_the_number_random = random.randint(1, 100)
    if "guess_count" not in st.session_state:
        st.session_state.guess_count = 0

    # User Guess Input
    user_guess = st.number_input(
        "Guess the number between 1 to 100",
        min_value=1,
        max_value=100,
        value=None,
        key="guess_input",
        placeholder="Enter a number between 1 and 100."
    )

    # Define Columns for Buttons
    col1, col2 = st.columns([2, 1])

    with col1:
        # Guess Button
        guess_button = st.button("Guess a Number", key="guess_button", use_container_width=True)

    with col2:
        # Reset Button
        if st.button("Reset the Game", key="reset_button", use_container_width=True):
            st.session_state.guessing_the_number_random = random.randint(1, 100)
            st.session_state.guess_count = 0
            st.rerun()

    # Check Guess Number
    if guess_button:
        if user_guess is None:
            st.error("Please enter a number")
        elif user_guess < 1 or user_guess > 100:
            st.warning("Please enter a number between 1 to 100")
        else:
            st.session_state.guess_count += 1
            if user_guess < st.session_state.guessing_the_number_random:
                st.error(f"Your guess is too low! \n Try Again")
            elif user_guess > st.session_state.guessing_the_number_random:
                st.error(f"Your guess is too high! \n Try Again")
            else:
                st.success(f"Congratulations! You guessed the number in {st.session_state.guess_count} attempts!")
                st.balloons()

    # Attempts Counter
    with st.container(border=True):
        st.title(":rainbow[Attempts]")
        st.write(f"**Attempts:** {st.session_state.guess_count}")

# Run the game
if __name__ == "__main__":
    guess_the_number()