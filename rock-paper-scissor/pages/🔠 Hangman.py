import streamlit as st
import random
from diagram import lives_visual_dict


def initialize_game():
    if "secret_word" not in st.session_state:
        st.session_state.secret_word = random.choice(["zoha","ayesha","huma","amna"])

    if "store_dash" not in st.session_state:
        st.session_state.store_dash = ["_"] * len(st.session_state.secret_word)

    if "lives" not in st.session_state:
        st.session_state.lives = 7

def display_game_status():
    st.title("🔠 :rainbow[Hangman Game]")
    st.subheader(f"Guess the Word: {' '.join(st.session_state.store_dash)}")
    container = st.container(border=True)
    # container.code(f"{lives_visual_dict[st.session_state.lives]}")
    container.code(lives_visual_dict[st.session_state.lives], language="plaintext")
    container.write(f"**Remaining Lives:** {st.session_state.lives}")


def process_guess(user_guess):
    if st.session_state.lives <= 0:
        st.error("💀 Game Over! Please reset the game to play again.")
        return
    

    if not user_guess or len(user_guess) != 1:
        st.warning("⚠️ Please enter a single letter.")
        return
    
    if user_guess in st.session_state.store_dash:
        st.info("ℹ️ You already guessed this letter.")
        return
    
    if user_guess in st.session_state.secret_word:
        for index, letter in enumerate(st.session_state.secret_word):
            if letter == user_guess:
                st.session_state.store_dash[index] = user_guess
        st.success("✅ Correct Guess!")
    else:
        if st.session_state.lives != 0 :
            st.session_state.lives -= 1
            st.error("❌ Wrong Guess!")
        
    if "_" not in st.session_state.store_dash:
        st.balloons()
        st.success("🎉 Congratulations! You guessed the word!")
        return
    st.rerun()
   
   
def reset_game():
    st.session_state.secret_word = random.choice(["zoha","ayesha","huma","amna"])
    st.session_state.store_dash = ["_"] * len(st.session_state.secret_word)
    st.session_state.lives = 7
    st.success("🔄 Game Reset!")
    st.rerun()



def main():
        
    initialize_game()
    display_game_status()

    user_guess = st.text_input("Enter a letter:", max_chars=1).upper()

    with st.container(border=True):
        col1, col2 = st.columns(2)

    with col1:
        if st.button("Check Letter", use_container_width=True):
            process_guess(user_guess)

    with col2:
        if st.button("Reset Game 🔄", use_container_width=True):
            reset_game()
            st.rerun()

if __name__ == "__main__":
    main()



















