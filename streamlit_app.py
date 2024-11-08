import streamlit as st

st.title("Hi! I am Streamlit Web App")
st.subheader("Hi! am your subheader")
st.header("I am Header")

st.text("Hi! I am a text function and programmers use me in place of paragraph tags")

st.markdown("**Hello** world") 
#    This is used for writing code in the form of html
# ** is used to signify bold text
# *  is used to signify italic text
# Go to https://www.markdownguide.org/cheat-sheet/

st.markdown("---") # This is used to input a breaking line in the text

st.caption("Hi I am a caption") #This is used to depict a caption.

# If you want to write a mathematical expression, use:
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")
# for more, visit https://www.katex.org/docs/supported.html

# Json function allows us add a json cord in our web app
json = {"a":"1,2,3", "b":"4,5,6"}
st.json(json)

# Code function allows the programmer display code on the web app
code = """
print("hello world")
def add(a, b):
    return a + b
"""
st.code(code, language="python") # displays the contents of "code" as a code

st.write("## H2")
st.metric(label="Wind Speed", value="120ms\^-1", delta="-1.4ms\^-1")

