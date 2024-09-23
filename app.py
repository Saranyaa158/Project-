import pickle
import streamlit as st  # type: ignore
import numpy as np  # type: ignore

st.header("BOOKS RECOMMENDER SYSTEM USING MACHINE LEARNING")

def load_data():
    try:
        model = pickle.load(open('artifacts/model.pkl', 'rb'))
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None, None, None, None

    try:
        books_name = pickle.load(open('artifacts/books_name.pkl', 'rb'))
    except Exception as e:
        st.error(f"Error loading books name: {e}")
        return model, None, None, None

    try:
        final_rating = pickle.load(open('artifacts/final_rating.pkl', 'rb'))
    except Exception as e:
        st.error(f"Error loading final ratings: {e}")
        return model, books_name, None, None

    try:
        book_pivot = pickle.load(open('artifacts/book_pivot.pkl', 'rb'))
    except Exception as e:
        st.error(f"Error loading book pivot: {e}")
        return model, books_name, final_rating, None 

    return model, books_name, final_rating, book_pivot

model, books_name, final_rating, book_pivot = load_data()



def fecth_poster(suggestions):
    poster_url = []
    for book_id in suggestions:
        book_name = book_pivot.index[book_id]
        # Check if the book name exists in final_rating
        ids = np.where(final_rating['title'] == book_name)[0]

        if ids.size > 0:  # Ensure there's a match
            idx = ids[0]  # Take the first index
            poster_url.append(final_rating.iloc[idx]['img_url'])
        else:
            st.warning(f"No poster found for '{book_name}'")  # Warning for missing posters

    return poster_url


           


def recommend_books(book_name):
    book_list = []
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distance, suggestions = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=6)

    poster_url = fecth_poster(suggestions.flatten())

    for i in range(len(suggestions)):
        books = book_pivot.index[suggestions[i]]
        book_list.extend(books)
        
    return book_list, poster_url



                
selected_books = st.selectbox("Type or select a book", books_name)


    
if st.button('Show Recommendation'):
    recommendation_books, poster_url = recommend_books(selected_books)
    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            st.text(recommendation_books[i])
            st.image(poster_url[i])
