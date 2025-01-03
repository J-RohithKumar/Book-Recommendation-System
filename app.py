#importing libraries
import streamlit as st
import numpy as np
import pandas as pd
import pickle as pkl

st.set_page_config(layout='wide')
st.header(':book: Book Recommendation System :computer:')
st.markdown("Using the data collected from Kaggle, we built a recommeder system. That suggests popular books as well as books you might liked based on your interest. Try it now. Open the sidebar get to know more :smile:")

top50_popular_books=pkl.load(open('./top50_popular_df.pkl','rb'))
book_with_ratings=pkl.load(open('./book_with_ratings.pkl','rb'))
similarity_scores=pkl.load(open('./similarity_scores.pkl','rb'))
books=pkl.load(open('./books.pkl','rb'))
ratings=pkl.load(open('./ratings.pkl','rb'))
users=pkl.load(open('./users.pkl','rb'))



# Popularity Based Recommendation

st.sidebar.title("Top 50 Popular Books")

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

# Collaborative Based Recommendation

def recommend_book(book_name):
  similar_books=similarity_scores[book_name].sort_values(ascending=False)[1:6].index
  data=book_with_ratings[book_with_ratings['Book-Title'].isin(similar_books)]
  return data[['Book-Title','Book-Author','Image-URL-M']].drop_duplicates('Book-Title').sort_values('Book-Title')

st.sidebar.title("Top 5 Books Based on your Interest")

list_of_books=similarity_scores.index
selected_book=st.sidebar.selectbox("Select a favourite books from the list",list_of_books)

if st.sidebar.button('Recommend Now'):
    recommend_books=recommend_book(selected_book)
    columns=5
    rows=10
    for row in range(rows):
        column=st.columns(columns)
        for col in range(columns):
            book_id=row*columns+col
            if book_id<len(recommend_books):
                with column[col]:
                    st.image(recommend_books.iloc[book_id]['Image-URL-M'])
                    st.text(recommend_books.iloc[book_id]['Book-Title'])
                    st.text(recommend_books.iloc[book_id]['Book-Author'])

# Done with Recommendation System. Now we can even display the data we have used, if needed

st.sidebar.title("Checkout Database")
if st.sidebar.button("Show Data"):
    st.subheader("Books Data")
    st.dataframe(books)
    st.divider()
    st.subheader("Book ratings")
    st.dataframe(ratings)
    st.divider()
    st.subheader("Users Data")
    st.dataframe(users)

# Social Links Section
st.sidebar.title("Know More")
col1,col2,col3=st.sidebar.columns(3)
col1.link_button("Colab","https://colab.research.google.com/drive/1AyOjDY6ocX9kOpWw_TFwijQf6D_Tg2Jg?usp=sharing")
col2.link_button("Github","https://github.com/J-RohithKumar/Book-Recommendation-System")
col3.link_button("LinkedIn","https://www.linkedin.com/in/rohithkumarjupalle/")