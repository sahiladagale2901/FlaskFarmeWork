import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

age = st.slider("Select your age: ", 0, 25, 100)

name = st.text_input("Enter your name:")

options = ["Java", "Python", "C#", "C++", "Js"]
choice = st.selectbox("Choose your favorite language: ", options)

if name:
    st.write(f"Hello, {str.capitalize(name)}")

st.write(f"Your age is {age}.")
st.write(f"Your favorite language is {choice}.")

data = {
    'Name': ['Jhon', 'Jane', 'Jake', 'Jill'],
    "Age": [28, 24, 35, 40],
    "City": ['New York', 'los Angeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(data)
df.to_csv("Sample.csv")
st.write(df)

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
