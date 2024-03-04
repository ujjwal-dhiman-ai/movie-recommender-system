import streamlit as st
import requests as re
import pickle

class MovieRecommender:
    def __init__(self, movies_path='model/movies_list.pkl', similarity_path='model/similarity.pkl'):
        self.movies = pickle.load(open(movies_path, 'rb'), encoding='latin1')
        self.similarity = pickle.load(open(similarity_path, 'rb'))

    def recommend(self, movie):
        index = self.movies[self.movies['title'] == movie].index[0]
        distances = sorted(
            list(enumerate(self.similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_movie_names = [
            self.movies.iloc[i[0]].title for i in distances[1:6]]
        return recommended_movie_names


def main():
    # Instantiate the MovieRecommender class
    movie_recommender = MovieRecommender()

    st.header('Movie Recommender System')

    movie_list = movie_recommender.movies['title'].values
    selected_movie = st.selectbox(
        "Type or select a movie from the dropdown",
        movie_list
    )

    if st.button('Show Recommendation'):
        recommended_movie_names = movie_recommender.recommend(selected_movie)
        for movie in recommended_movie_names:
            st.text(movie)


if __name__ == "__main__":
    main()
