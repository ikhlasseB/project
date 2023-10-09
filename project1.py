import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

df = pd.read_excel(r'C:\Users\HP\Desktop\PTJ\Excel_Feature Use in Courses.xlsx')

st.title("Course Counts Analysis")
st.sidebar.title("Select a School and a Course")

st.write("**Course Counts for All Courses**")
st.bar_chart(df[["Course ID", "Count"]].set_index("Course ID"), color='#009639')

school_names = df["Account Name"].unique()
school = st.sidebar.selectbox("Select a School", school_names)

new_df1 = df[df["Account Name"] == school]
course_names = new_df1["Course Name"]
course = st.sidebar.selectbox("Select a Course", course_names)

new_df2 = df[df["Course Name"] == course]
count = new_df2["Count"].values[0]
st.write(f"##### Count for **`{course}`**: **`{count}`**")
