import pandas as pd
import streamlit as st



# Calculation
def calculation(weight,height):
    bmi = weight / ((height/100)**2)
    st.write(f"### **Your BMI:** is {bmi:.2f}")

    if bmi < 16:
        st.error("⚠️ You are **Severely Underweight**")
    elif bmi < 18.5:
        st.warning("⚠️ You are **Underweight**")
    elif bmi < 25:
        st.success("✅ You have a **Healthy Weight** 🎉")
    elif bmi < 30:
        st.warning("⚠️ You are **Overweight**")
    else:
        st.error("⚠️ You are **Obese**")



#  Categories Tips
def bmi_categories_tips():
    
    st.write("## 📊 BMI Categories & Tips")
    
    bmi_data = {
        "Category": [
            "⚠️ Severely Underweight",
            "⚠️ Underweight",
            "✅ Healthy Weight 🎉",
            "⚠️ Overweight",
            "⚠️ Obese"
        ],
        "BMI Range": [
            "Below 16",
            "16 - 18.4",
            "18.5 - 24.9",
            "25 - 29.9",
            "30 & Above"
        ],
        "Health Tips 🏥": [
            "Increase calorie intake & consult a doctor.",
            "Eat balanced meals, exercise lightly.",
            "Maintain a healthy lifestyle! 🏆",
            "Exercise regularly, watch your diet.",
            "Consult a doctor & focus on weight management."
        ]
    }

    df = pd.DataFrame(bmi_data)
    st.dataframe(df)  



# BMI UI
def main():
    st.title("🏋️‍♂️ :rainbow[BMI Calculator]")
    st.write("Calculate your Body Mass Index (BMI) and understand your health category.")


    weight= st.select_slider("⚖️ Select Your Weight (KG)",options=list(range(30,151)),)
    height= st.select_slider("📏 Select Your Height (cm)",options=list(range(100,201)),)

    if st.button("🎯 Calculate BMI"):
        calculation(weight,height)

    bmi_categories_tips()

    
if __name__ == '__main__':
    main()
  
   
