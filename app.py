import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("food_data.csv")
# Food emojis
food_emoji = {
    "Rice": "🍚",
    "Chapati": "🫓",
    "Pizza": "🍕",
    "Burger": "🍔",
    "Apple": "🍎",
    "Banana": "🍌",
    "Egg": "🥚",
    "Milk": "🥛"
}

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

food = st.selectbox(
    "Select Food",
    df["Food"],
    format_func=lambda x: f"{food_emoji.get(x, '')} {x}"
)

calories = df[df["Food"] == food]["Calories"].values[0]
cat = category(calories)

st.subheader(f"{food_emoji.get(food, '')} {food} → 🔥 {calories} Calories")
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

    # ✅ ONLY ONE BLOCK (fixed)
    if bmi < 18.5:
        st.warning("Underweight - Increase healthy calorie intake 🥗")
    elif bmi < 25:
        st.success("Normal weight - Maintain your lifestyle ✅")
    else:
        st.error("Overweight - Try reducing high-calorie foods and stay active 🏃")

# DAILY CALORIES
st.header("🍽 Daily Calorie Counter")

foods = st.multiselect(
    "🍽 Select foods you ate",
    df["Food"],
    format_func=lambda x: f"{food_emoji.get(x, '')} {x}"
)
total = df[df["Food"].isin(foods)]["Calories"].sum()

st.subheader(f"🔥 Total Calories Consumed: {total}")

if total > 500:
    st.error("⚠️ High calorie intake today! Stay active 🏃")
elif total > 200:
    st.info("⚖️ Moderate intake 👍")
elif total > 0:
    st.success("🥗 Healthy eating today! Great job ✅")


    
