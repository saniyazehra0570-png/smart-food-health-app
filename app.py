import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("food_data.csv")

# Functions
def category(cal):
    if cal < 100:
        return "Low"
    elif cal < 250:
        return "Medium"
    else:
        return "High"

def bmi_calc(weight, height):
    return weight / (height ** 2)

# Title
st.title("🥗 Smart Food & Health Advisor")

# FOOD SECTION
st.header("🍔 Food Calorie Checker")

food = st.selectbox("Select Food", df["Food"])

calories = df[df["Food"] == food]["Calories"].values[0]
cat = category(calories)

st.write(f"Calories: {calories}")

if cat == "High":
    st.warning("⚠️ Eat in moderation")
elif cat == "Medium":
    st.info("👍 Moderate consumption")
else:
    st.success("✅ Healthy choice")

st.bar_chart(df.set_index("Food"))

# BMI SECTION
st.header("⚖️ BMI Calculator")

weight = st.number_input("Enter weight (kg)", min_value=1.0)
height = st.number_input("Enter height (meters)", min_value=0.5)

if st.button("Calculate BMI"):
    bmi = bmi_calc(weight, height)
    st.subheader(f"Your BMI: {bmi:.2f}") 
    if bmi < 18.5:
        st.warning("Underweight - Increase healthy calorie intake 🥗")
    elif bmi < 25:
        st.success("Normal weight - Maintain your lifestyle ✅")
    else:
        st.error("Overweight - Try reducing high-calorie foods and stay active 🏃")

    if bmi < 18.5:
        st.warning("Underweight")
    elif bmi < 25:
        st.success("Normal weight")
    else:
        st.error("Overweight")

# DAILY CALORIES
st.header("🍽 Daily Calorie Counter")

foods = st.multiselect("Select foods you ate", df["Food"])
total = df[df["Food"].isin(foods)]["Calories"].sum()

st.write(f"Total Calories: {total}")
