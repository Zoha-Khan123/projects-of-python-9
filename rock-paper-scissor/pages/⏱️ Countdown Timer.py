import streamlit as st
import time


def countdown_timer():
    st.title("⏱️ Countdown Timer")
    st.write("Set a timer and let it count down!")
    t = int(st.select_slider("⏳ Select Countdown Time (seconds)",options=list(range(0,11))))
    start_button = st.button("Start Countdown")


    if start_button:
        timer_placeholder = st.empty()
        while t > 0:
            secs = t
            timer_placeholder.write(f"### ⏳ Time Left: **`{secs:02d}` seconds**")
            time.sleep(1)
            t -= 1

        timer_placeholder.write("### 🎉 **Time's UP!** ")
        st.balloons()
  
countdown_timer()
