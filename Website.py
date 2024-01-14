import streamlit as st 
import json
from streamlit_lottie import st_lottie
st.set_page_config(
    page_title='Multipage App',layout='wide'
)
left_column, right_column = st.columns(2)
with left_column:
    with left_column:
        st.title('')
        st.title('')
        st.title("Global Conflict:")


st.sidebar.success('Select a page above.')
def get(path:str):
    with open(path,"r") as p:
        return json.load(p)
path=get("./fe.json.json")

with right_column:
    st_lottie(path,height=650,key='coding',loop=True)
with left_column:
    st.subheader("Global conflict is a term that refers to the state of hostility,\
              violence, or war between different countries, regions, groups, or \
             ideologies.")
    st.subheader("Global conflict can have various causes, such as political,\
             economic, religious, ethnic, or environmental factors. Global conflict \
            can also have various effects, such as human suffering, displacement, \
            migration, terrorism, poverty, inequality, or environmental degradation.")
    st.title('')
    st.title('')
    st.title('')

with right_column:
    
    st.title('"The idea that nations    and peoples could come\
                   together in peace to solve their disputes and\
               advance a common prosperity seemed unimaginable. \
               It took the awful carnage of two world wars to shift our way of thinking."')
with left_column:
    st.image("obama.png",caption='Former President of the United States, Barack Obama')