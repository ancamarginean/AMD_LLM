import streamlit as st
import pandas as pd
import numpy as np



st.set_page_config(
    layout="wide",
)

#



st.title("LLMs generated answers for AMD questions")


st.write("Choose one of the applications on the left")

st.write("""Experiments published in paper: 
Muntean, G.A.; Marginean, A.; Groza, A.; Damian, I.; Roman, S.A.; Hapca, M.C.; Sere, A.M.; Mănoiu, R.M.; Muntean, M.V.; Nicoară, S.D. 
A Qualitative Evaluation of ChatGPT4 and PaLM2’s Response to Patient’s Questions Regarding Age-Related Macular Degeneration. 
Diagnostics 2024, 14, 1468. 
https://doi.org/10.3390/diagnostics14141468
""")