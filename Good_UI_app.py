import streamlit as st
import pickle
import pandas as pd
import requests

# --- Premium Dark Theme CSS ---
st.markdown("""
    <style>
    /* Background */
    body {
        background: linear-gradient(135deg, #1f1c2c, #928dab);
        color: #e0e0e0;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    /* Container padding fix */
    .css-18e3th9 {
        padding-top: 1rem;
        padding-bottom: 3rem;
    }
    /* Title */
    h1 {
        color: #61dafb !important;
        text-align: center;
        font-weight: 900;
        margin-bottom: 2rem;
        text-shadow: 0 0 8px #61dafb88;
        white-space: nowrap; /* keep in one line */
        overflow: hidden;
        text-overflow: ellipsis;
    }
    /* Movie card */
    .movie-card {
        background: #2c2a4a;
        padding: 12px 10px 16px 10px;
        border-radius: 14px;
        box-shadow: 0 6px 18px rgba(97, 218, 251, 0.4);
        text-align: center;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        animation: fadeIn 0.7s ease forwards;
        color: #e0e0e0;
    }
    .movie-card:hover {
        transform: scale(1.07);
        box-shadow: 0 12px 30px rgba(97, 218, 251, 0.75);
        cursor: pointer;
    }
    /* Movie title */
    .movie-title {
        font-size: 14px;
        font-weight: 700;
        color: #61dafb;
        padding-bottom: 6px;
        margin-bottom: 14px;
        border-bottom: 3px solid #61dafb;
        text-align: center;
        transition: color 0.3s ease;
        user-select: none;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }
    .movie-title:hover {
        color: #21a1f1;
    }
    /* FadeIn Animation */
    @keyframes fadeIn {
        0% {opacity: 0; transform: translateY(20px);}
        100% {opacity: 1; transform: translateY(0);}
    }
    </style>
""", unsafe_allow_html=True)


# --- Poster Fetcher ---
def fetch_poster(movie_id):
    api_key = "c045906aff714aa0a4a4ad9f208512df"
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
    response = requests.get(url)
    data = response.json()
    poster_path = data.get('poster_path')
    if poster_path:
        return "https://image.tmdb.org/t/p/w500" + poster_path
    else:
        return "https://via.placeholder.com/300x450?text=No+Image"


# --- Recommendation Logic ---
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters


# --- Load Data ---
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# --- Streamlit UI ---
st.markdown("<h1> Movie Recommendation System</h1>", unsafe_allow_html=True)

selected_movie_name = st.selectbox('🔍 Choose a Movie You Like:', movies['title'].values)

if st.button('Recommend Similar Movies'):
    names, posters = recommend(selected_movie_name)
    st.markdown("<h2 style='color: #61dafb; margin-top: 20px;'>Top 5 Recommendations:</h2>", unsafe_allow_html=True)

    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.markdown(f"<div class='movie-card'>"
                        f"<div class='movie-title' title='{names[idx]}'>{names[idx]}</div>", unsafe_allow_html=True)
            st.image(posters[idx], use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)
