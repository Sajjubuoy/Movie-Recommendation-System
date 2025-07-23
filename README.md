Movie Recommendation System
This is a simple content-based movie recommender system built using Python, NLP, and machine learning concepts. The system suggests similar movies based on your input using a technique called cosine similarity on text-based features.

 What the Project Does
 
# Takes a movie title as input.
# Analyzes its genre, cast, crew, keywords, and description.
# Recommends 5 similar movies.
#Also displays movie posters using The Movie Database (TMDb) API.

 Project Structure
This project has two main parts:

1. Backend (Data Processing & Recommendation Logic)
Step-by-Step Workflow:
Import Libraries
Use libraries like pandas, numpy, ast, scikit-learn, and pickle.

Load Data
Load two CSV files:

tmdb_5000_movies.csv

tmdb_5000_credits.csv

Merge Datasets
Combine both datasets on the movie title column.

Select Relevant Features
Use only the columns required for recommendation:
movie_id, title, overview, genres, keywords, cast, crew.

Clean and Parse Data

Convert stringified JSON columns into Python lists using ast.literal_eval.

Extract top 3 cast members.

Extract only the director from the crew.

Remove spaces from multi-word names (e.g., "Science Fiction" → "ScienceFiction").

Create Tags
Combine overview, genres, keywords, cast, and crew into one text column called tags.

Text Vectorization
Use CountVectorizer to convert tags into vectors (bag-of-words representation).

Similarity Calculation
Use cosine_similarity to compute similarity between movies based on tag vectors.

Recommend Function
Given a movie name, return the top 5 most similar movie titles.

Save Models
Use pickle to save:

movie_list.pkl (movie titles and metadata)

similarity.pkl (precomputed similarity matrix)

2. Frontend (Streamlit Web App)
Features:
Dropdown Menu
Lets users select or type a movie name.

Show Recommendation Button
Displays 5 similar movies when clicked.

Movie Posters
Uses TMDb API to fetch and display posters for each recommended movie.

 Concepts Used
#Natural Language Processing (NLP)
#Bag-of-Words Model
#CountVectorizer
#Cosine Similarity
#JSON Parsing using ast.literal_eval()
#Content-Based Filtering

 Technologies Used
#Python
#pandas, numpy, scikit-learn
#Streamlit (for UI)
#TMDb API (for poster images)
#Pickle (for saving models)



Mail me @kmahammadsajjda@gmail.com for any doubts, i will clarify your doubts in simple way
Happy Learning!
