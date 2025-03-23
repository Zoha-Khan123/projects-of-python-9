import  streamlit as st 

emoji_dict = {
    "elephant": "🐘",
    "lion": "🦁",
    "cat": "🐱",
    "dog": "🐶",
    "monkey": "🐵",
    "jungle": "🌳",
    "beach": "🏖️",
    "city": "🏙️",
    "dancing": "💃",
    "running": "🏃",
    "jumping": "🤾",
    "red": "🔴",
    "blue": "🔵",
    "green": "🟢",
}

# Story Making
def make_story(animal,verb,color,place):
    animal_emoji = emoji_dict.get(animal, "❓")
    verb_emoji = emoji_dict.get(verb, "❓")
    color_emoji = emoji_dict.get(color, "❓")
    place_emoji = emoji_dict.get(place, "❓")

    
    story = f"""
    📝 **:rainbow[Your Funny Emoji Story]** 🎭  

    It was a beautiful day when I decided to visit the **{place}** {place_emoji}.  
    As I was walking, I suddenly spotted a **{color}** {color_emoji} **{animal}** {animal_emoji}.  
    To my surprise, it was **{verb}** {verb_emoji} happily!  
    Everyone around was amazed to see a **{animal}** {animal_emoji} behaving like that in the **{place}** {place_emoji}.  
    I quickly took out my phone to capture this rare moment.  
    _It was a day I will never forget!_ 🎥✨
    """
    return story
    


# Mad Lib UI
def main():
    st.title("🎭 :rainbow[ Fun Emoji Mad Libs] 🎉")

    with st.form("my_form"):
        st.write("Fill in the blanks and see a funny story with matching emojis!")

        animal = st.selectbox("Select an animal" , ["elephant", "lion", "cat", "dog", "monkey"])
        verb = st.selectbox("Choose a verb:", ["dancing", "running", "jumping"])
        color = st.selectbox("Choose a color:", ["red", "blue", "green"])
        place = st.selectbox("Choose a place:", ["jungle", "beach", "city"])
        submitted = st.form_submit_button('Generate Story')

        if submitted:
            story = make_story(animal,verb,color,place)
            container = st.container(border=True)
            container.write(story)


if __name__ == '__main__':
    main()















