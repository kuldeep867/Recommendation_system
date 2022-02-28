import pickle
import streamlit as st
import pandas as pd

st.set_page_config(
     page_title="Ex-stream-ly Cool App",
     layout="wide",
 )

def recommend(x):
    index=drama[drama['Title'] == x ].index[0]
    distances=similarity[index]
    drama_list   = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])[1:6]

    recommend_drama_list=[]
    for i in drama_list:
        recommend_drama_list.append(drama.iloc[i[0]].Title)
    return recommend_drama_list

st.image("yellow-flower-fence-dark-black-background-ex.jpg",use_column_width=True)
model=pickle.load(open('movie_dict.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))

drama=pd.DataFrame(model)

st.title("Welcome to Korean drama recommender system")

selecter_drama_name=st.selectbox(" ",drama['Title'].values)

if st.button('Recommend'):
    output=recommend(selecter_drama_name)
    for i in output:
        st.write(i)


st.image("1600px_COLOURBOX38553892.jpg",use_column_width=True)
