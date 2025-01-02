#importing libraries
import streamlit as st
import numpy as np
import pandas as pd
import pickle as pkl
st.set_page_config(layout='wide')

st.header('Book Recommendation System')

top50_popular_books=pkl.load(open('./top50_popular_df.pkl','rb'))
book_with_ratings=pkl.load(open('./book_with_ratings.pkl','rb'))
# recommend_book=pkl.load(open('./recommend_book.pkl','rb'))
similarity_scores=pkl.load(open('./similarity_scores.pkl','rb'))



st.sidebar.title("Top 50 Books")

if st.sidebar.button('Show'):
    columns=5
    rows=10
    for row in range(rows):
        column=st.columns(columns)
        for col in range(columns):
            book_id=row*columns+col
            if book_id<len(top50_popular_books):
                with column[col]:
                    st.image(top50_popular_books.iloc[book_id]['Image-URL-M'])
                    st.text(top50_popular_books.iloc[book_id]['Book-Title'])
                    st.text(top50_popular_books.iloc[book_id]['Book-Author'])
