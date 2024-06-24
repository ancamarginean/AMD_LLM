import streamlit as st
import pandas as pd

st.set_page_config(
    layout="wide",
)

DATA_URL = "./used_in_paper.csv"
@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)

    return data


@st.cache_data
def load_new_data(nrows):
    data = pd.read_csv("./gpt4_2.csv", nrows=nrows)
    data.columns = ["id", "type", "question", "answer"]
    data["question"] = data["question"].str.strip()
    return data

criterii = ["Reflects clinical and scientific consensus", "Low likelihood of harm", "Correct reasoning",
      "Correct reading comprehension", "Relevant content", "Not missing important information"]
criterii2=[f"{c}.1" for c in criterii]

data=load_data(1000)
new_data=load_new_data(1000)

option = st.selectbox(
    "Choose a question to get further details",
    data[~data["Question"].isnull()]["Question"].values,
    index=None,
    placeholder="Select a question...")

if option:
    qno = data[data["Question"]==option]["qno"].values[0]
    d = data[data["qno"]==qno]
    st.write(option)

    col1, col2, = st.columns(2)
    with col1:
        container = st.container(border=True)
        container.write("GPT4 December 2023:")
        container.write(d["GPT4"].values[0])
    with col2:
        container = st.container(border=True)
        container.write("GPT2 June 2024")
        container.write(new_data[new_data["question"]==option]["answer"].values[0])

    col1, col2, = st.columns(2)
    with col1:
        header1, header2, header3 = st.columns(3)
        with header1:
            st.subheader("Evaluation Criteria")
        with header2:
            st.subheader("Reviewer 1")
        with header3:
            st.subheader("Reviewer 2")
        for c in criterii:
            col11, col12, col13 = st.columns(3)
            with col11:
                st.write(f"{c}")
            with col12:
                st.write(f' {d[d["Unnamed: 4"]=="Reviewer 1"][c].values[0]}')
            with col13:
                st.write(f' {d[d["Unnamed: 4"] == "Reviewer 2"][c].values[0]}')

    # with col2:

        # header1, header2, header3 = st.columns(3)
        # with header1:
        #     st.subheader("Evaluation Criteria")
        # with header2:
        #     st.subheader("Reviewer 1")
        # with header3:
        #     st.subheader("Reviewer 2")
        # for c in criterii2:
        #     col11, col12, col13 = st.columns(3)
        #     with col11:
        #         st.write(f"{c.split('.')[0]}")
        #     with col12:
        #         st.write(f' {d[d["Unnamed: 4"] == "Reviewer 1"][c].values[0]}')
        #     with col13:
        #         st.write(f' {d[d["Unnamed: 4"] == "Reviewer 2"][c].values[0]}')

    container = st.container(border=True)
    container.write("Physician 1:")
    container.write(d["Ioana"].values[0])

    container = st.container(border=True)
    container.write("Physician 2:")
    container.write(d["Roxana"].values[0])


    container = st.container(border=True)
    container.write("Physician 3:")
    container.write(d["Madalina"].values[0])