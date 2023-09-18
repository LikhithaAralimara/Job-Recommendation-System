import streamlit as st
import pandas as pd
import pickle as pc


df= pc.load(open('df.pkl','rb'))
similarity = pc.load(open('similarity.pkl','rb'))


def recommendation(title):
    idx=df[df['Title']==title].index[0]
    idx = df.index.get_loc(idx)
    distances=sorted(list(enumerate(similarity[idx])),reverse=True,key=lambda x:x[1])[1:22]

    jobs = []
    for i in distances:
        jobs.append(df.iloc[i[0]].Title)
    
    return jobs


#web app 
st.write("Likhitha Aralimara")
st.title('Job Recommendation System')
title = st.selectbox('search job',df['Title'])

jobs=recommendation(title)

if jobs:
    st.write(jobs)
