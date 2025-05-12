import streamlit as st
import pickle
import numpy as np

# Wide layout
st.set_page_config(layout="wide")

# Header
st.markdown("<h1 style='text-align: center; color: #3b3b3b;'>📚 Book Recommendation System</h1>", unsafe_allow_html=True)

# Load data and model
model = pickle.load(open('artifacts/model.pkl','rb'))
book_names = pickle.load(open('artifacts/book_names.pkl','rb'))
final_rating = pickle.load(open('artifacts/final_rating.pkl','rb'))
book_pivot = pickle.load(open('artifacts/book_pivot.pkl','rb'))

# Function to fetch image URLs
def fetch_poster(suggestion):
    book_name = []
    ids_index = []
    poster_url = []

    for book_id in suggestion:
        book_name.append(book_pivot.index[book_id])

    for name in book_name[0]: 
        ids = np.where(final_rating['title'] == name)[0][0]
        ids_index.append(ids)

    for idx in ids_index:
        url = final_rating.iloc[idx]['image_url']
        poster_url.append(url)

    return poster_url

# Function to recommend books
def recommend_book(book_name):
    books_list = []
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1), n_neighbors=6)
    poster_url = fetch_poster(suggestion)

    for i in range(len(suggestion)):
        books = book_pivot.index[suggestion[i]]
        for j in books:
            books_list.append(j)
    return books_list, poster_url       

# ----------------- Custom CSS --------------------
# ----------------- Custom CSS --------------------
st.markdown("""
    <style>
        .book-card {
            background-color: #f0f0f5;
            padding: 0.8rem;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            cursor: default;  /* Prevents pointer/plus cursor */
        }
        .book-card:hover {
            transform: translateY(-6px);
            box-shadow: 0 10px 24px rgba(0, 0, 0, 0.12);
        }
        .book-title {
            font-size: 0.875rem;
            font-weight: 600;
            color: #333333;
            margin-bottom: 8px;
            cursor: default;  /* Ensures title is non-clickable */
        }
        .css-1kyxreq {
            font-size: 22px !important;
            font-weight: 600;
            color: #333333;
        }
        div.stButton > button {
            background-color: #a6a6a6;
            color: white;
            padding: 0.5em 1.3em;
            border-radius: 6px;
            font-size: 14px;
            font-weight: 600;
            border: none;
            transition: 0.3s ease-in-out;
        }
        div.stButton > button:hover {
            background-color: #8c8c8c;
            color: #ffffff;
            transform: scale(1.02);
        }

        /* Disable click and pointer for all children of book card */
        .book-card * {
            pointer-events: none;
            cursor: default;
        }
    </style>
""", unsafe_allow_html=True)

# ----------------- Select Box and Button --------------------
selected_books = st.selectbox("📖 Select a Book", book_names)

if st.button("🔍 Show Recommendations"):
    recommended_books, poster_url = recommend_book(selected_books)
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.markdown(f"""
                <div class='book-card'>
                    <div class='book-title'>{recommended_books[i+1]}</div>
                    <img src='{poster_url[i+1]}' width='148' height='218' style='border-radius: 4px; margin-top: 6px;'>
                </div>
            """, unsafe_allow_html=True)
