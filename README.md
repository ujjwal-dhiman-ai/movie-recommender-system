# Movie Recommender System

This project is a movie recommender system built using Python, Streamlit, and the Scikit-learn library. The system recommends similar movies based on user input, allowing users to receive suggestions for films related to their preferences.

## Technologies Used

- Python: The primary programming language used for building the application and developing the machine learning model.

- Streamlit: The web application framework used for creating the user interface and deploying the recommender system.

- Scikit-learn: The machine learning library employed for developing the recommendation model.

## Overview
The recommender system follows a step-by-step process, utilizing a dataset of 5000 movies from Kaggle. The main steps in the model development include:

### Data Reading:

- Imported a dataset containing information about 5000 movies from Kaggle.

### Feature Selection:

- Focused on text features that are likely to contribute to the recommendation process.
- Selected features: "genres," "keywords," "title," "overview," "cast," and "crew."

### Data Cleaning:

- Checked for null and duplicate values in the dataset to ensure data integrity.

### Data Transformation:

- Transformed the text features to prepare them for model building.
- Converted raw text values into list format.
- Extracted relevant information from raw data.
- Removed white spaces between words.
- Created a new feature called "tags" by merging all relevant text features.
### Word Stemming:

- Applied stemming to transform words into their root form.
- Utilized the NLTK library with the PorterStemmer algorithm.

### Model Development:

- Vectorized the features using the CountVectorizer algorithm from Scikit-learn.
- Utilized Cosine Similarity for searching and recommending the most similar movies based on user input.

## How to Use

### Clone the repository to your local machine:

- ``` git clone https://github.com/your-username/movie-recommender.git```

### Install Dependencies:

- Make sure you have the required dependencies installed. You can use the following command:
``` pip install -r requirements.txt ```

### Run the App:

- Execute the following command to run the Streamlit web application:
``` streamlit run app.py ```
- This will start a local server, and you can access the movie recommender system through your web browser.
  
### Input Movie Name:

- Enter the name of a movie you like into the provided input field.
- Get Recommendations:
  - The system will recommend 5 similar movies based on the input you provided.

### Explore Recommendations:

- Explore the recommended movies and discover new films that match your preferences.
Feel free to explore and enhance the project based on your preferences and requirements. Happy movie watching!





