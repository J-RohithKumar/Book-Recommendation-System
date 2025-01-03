# Book Recommendation System

This project is a **Book Recommendation System** that uses collaborative filtering and content-based filtering techniques to provide personalized book recommendations. The system is powered by preprocessed datasets and similarity scores for accurate and efficient recommendations.

## Live Demo

Check out the live version of this project here: [Book Recommendation System](https://book-recommendation-system-webapp.streamlit.app/)


## Getting Started
Follow these instructions to clone and run the project locally.
### Prerequisites
- [Git](https://nodejs.org/en) for cloning the repository
- [Python 3](https://www.python.org/) and [pip](https://pip.pypa.io/en/stable/) for the libraries
- [Streamlit](https://streamlit.io/) for web application interface
### Cloning the Repository
- Open your terminal and clone the repository using the following command : 
    
    `git clone https://github.com/J-RohithKumar/Book-Recommendation-System.git`
- Navigate into the project directory : `cd Book-Recommendation-System`

## Project Structure

```plaintext
BOOK-RECOMMENDATION-SYSTEM
│
├── app.py                     # Main script
├── book_with_ratings.pkl      # Data in pickle format
├── books.pkl                  # Data in pickle format
├── ratings.pkl                # Data in pickle format
├── users.pkl                  # Data in pickle format
├── similarity_scores.pkl      # Precomputed similarity scores
├── top50_popular_df.pkl       # Dataset of top 50 popular books
└── Readme.md                  # Documentation of project
```
## Installation

- Navigate : `cd Book-Recommendation-System`
- Install the required packages.
- Run the app : `streamlit run app.py`

## Technologies Used

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Google Colab](https://img.shields.io/badge/Google%20Colab-%23F9A825.svg?style=for-the-badge&logo=googlecolab&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-%23FE4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)


