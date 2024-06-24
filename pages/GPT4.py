import streamlit as st
import pandas as pd




st.set_page_config(
    layout="wide",
)


st.title("GPT4 generated answers for AMD questions")


criterii = ["Reflects clinical and scientific consensus", "Low likelihood of harm", "Correct reasoning",
      "Correct reading comprehension", "Relevant content", "Not missing important information"]
criterii2=[f"{c}.1" for c in criterii]
with st.expander("Legend for Evaluation Criteria:"):

    for i,c in enumerate(criterii):
        st.write(f"C{i+1} = {c} ")

DATA_URL = "./used_in_paper.csv"


columns=["type", "Question", "GPT4", "Unnamed: 4"]
columns2 = ["qno", "type", "Question", "GPT4"]

reviewer1 = "Reviewer 1"
reviewer2 = "Reviewer 2"





def show_details(qno):
    st.table(data[data["qno"]==qno][["Ioana", "Madalina", "Roxana"]])



@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    #data =
    #data = read_old()
    #lowercase = lambda x: str(x).lower()
    #data.rename(lowercase, axis='columns', inplace=True)

 #   data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data



data = load_data(1000)


# st.table(data)

def get_rev2(qno):
    return data[(data["qno"]==qno)&(data["Unnamed: 4"]=="Reviewer 2")]["grade"].values[0]
data["grade"] = "C1:"+data[criterii[0]].astype(str)+"\nC2:"+ data[criterii[1]].astype(str)+"\nC3:"+ \
                data[criterii[2]].astype(str)+"\nC4:"+data[criterii[3]].astype(str)+"\nC5:"+data[criterii[4]].astype(str)+"\nC6:"+data[criterii[5]].astype(str)
data["grade2"]=data.apply(lambda x: get_rev2(x["qno"]), axis=1)
data["grade"] = data["grade"].apply(lambda x: x.replace('\n', '<br>'))
data["grade2"] = data["grade2"].apply(lambda x: x.replace('\n', '<br>'))

#data = data[columns+["grade"]]
table_columns=columns2+["grade", "grade2"]
frame_columns=columns+criterii +["qno"]

st.sidebar.header("Question type")
unique_values = ["ALL"]+list(data['type'].unique())
selected_value = st.sidebar.selectbox("Select a value", unique_values)


# st.sidebar.header("View type")
# unique_views = ["dataframe", "table"]
# selected_view = st.sidebar.selectbox("Select a value", unique_views)

# st.sidebar.header("Reviewer")
# rev_values = [None, reviewer1, reviewer2]
# selected_rev = st.sidebar.selectbox("Select a reviewer", rev_values)

filtered_data = data[data['type'] == selected_value] if selected_value!="ALL" else data
#filtered_data = filtered_data[data['Unnamed: 4'] == selected_rev][columns2] if selected_rev else filtered_data[columns]




st.write(f"Filtered Data for {selected_value}")
#if selected_view=="table"::
if 1==1:
    f2 = filtered_data.dropna(subset="question")
    f2["GPT4"] = f2["GPT4"].apply(lambda x: x.replace('\n', '<br>'))

    st.markdown(f2[table_columns].to_html(escape=False, index=False), unsafe_allow_html=True)
# else:
#     # for i in range(len(data)):
#     #     with st.expander(f"Details for {data.loc[i, 'qno']}"):
#     #         show_details(data.loc[i, 'qno'])
#     st.dataframe(filtered_data[frame_columns])
