import streamlit as st
import pandas as pd

st.set_page_config(
    layout="wide",
)

st.subheader("Comparison between two GPT queries")
st.write("Common ideas are marked with common colors between left and right. ")

DATA_URL = "./comparison.csv"
@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)

    return data
data=load_data(200)
data = data.dropna(subset="question")
data["GPT4 DEC 2023"] = data["GPT4 DEC 2023"].apply(lambda x: x.replace('\n', '<br>'))
data["GPT4 JUN 2024"] = data["GPT4 JUN 2024"].apply(lambda x: x.replace('\n', '<br>'))
st.markdown(data.to_html(escape=False, index=False), unsafe_allow_html=True)

criterii = ["Reflects clinical and scientific consensus", "Low likelihood of harm", "Correct reasoning",
      "Correct reading comprehension", "Relevant content", "Not missing important information"]
criterii2=[f"{c}.1" for c in criterii]

data=load_data(1000)
