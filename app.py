import pickle
import streamlit as st
import numpy as np
import pandas as pd
import requests

st.header('Bollywood Movie Recommendation System')

movies=pd.read_pickle(open('bollywoodmovie_list.pkl','rb'))
similarity=pickle.load(open('moviesimilarity.pkl','rb'))

def fetch_poster(movie_title):
    url="https://www.omdbapi.com/?apikey=162c47f3&t={}".format(movie_title)
    data=requests.get(url)
    data=data.json()
    try:
        return data['Poster']
    except:
        return ""

def recommend(movie):
    index=movies[movies['movie_name']==movie].index[0]
    distance=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda x:x[1])
    movie_names=[]
    movie_images=[]
    for i in distance[1:6]:
        movie_title=movies.iloc[i[0]].movie_name
        #yr = movies.iloc[i[0]].year
        movie_names.append(movie_title)
        movie_images.append(fetch_poster(movie_title))
    return movie_names,movie_images

movie_list=np.sort(movies['movie_name'].values)

selected_movie = st.selectbox('Select Movie Name:',movie_list)

if st.button('Show Recommendation'):
    movie_names,movie_images=recommend(selected_movie)
    col1,col2,col3,col4,col5=st.beta_columns(5)

    with col1:
        st.text(movie_names[0])
        if(movie_images[0]!=""):
            st.image(movie_images[0])
        else:
            st.text("No Poster Found!")

    with col2:
        st.text(movie_names[1])
        if (movie_images[1] != ""):
            st.image(movie_images[1])
        else:
            st.text("No Poster Found!")

    with col3:
        st.text(movie_names[2])
        if (movie_images[2] != ""):
            st.image(movie_images[2])
        else:
            st.text("No Poster Found!")

    with col4:
        st.text(movie_names[3])
        if (movie_images[3] != ""):
            st.image(movie_images[3])
        else:
            st.text("No Poster Found!")

    with col5:
        st.text(movie_names[4])
        if (movie_images[4] != ""):
            st.image(movie_images[4])
        else:
            st.text("No Poster Found!")
