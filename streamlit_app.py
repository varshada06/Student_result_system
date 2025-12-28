
import streamlit as st
import pandas as pd

st.title("🎓 Student Result Processing System")

df = pd.read_csv("students.csv")

df["Total"] = df[["Maths", "Science", "English"]].sum(axis=1)
df["Percentage"] = df["Total"] / 3

def grade(p):
    if p >= 75:
        return "A"
    elif p >= 60:
        return "B"
    elif p >= 40:
        return "C"
    else:
        return "Fail"

df["Grade"] = df["Percentage"].apply(grade)
df["Status"] = df["Grade"].apply(lambda x: "Pass" if x != "Fail" else "Fail")

st.subheader("📊 Final Results")
st.dataframe(df)

topper = df.loc[df["Percentage"].idxmax()]
st.success(f"🏆 Topper: {topper['Name']} ({topper['Percentage']:.2f}%)")
