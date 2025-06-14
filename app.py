from flask import Flask, render_template, request, redirect, url_for
import pickle
import numpy as np

# Download large files if not present
import os
import requests

if not os.path.exists('books.pkl'):
    url = 'https://drive.google.com/file/d/16nuuFdnTyfNYZpWT10X96hkAQCk8uwcu/view'
    with open('books.pkl', 'wb') as f:
        f.write(requests.get(url).content)

# Load necessary data
popular_df = pickle.load(open('popular.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           book_name=list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['num_ratings'].values),
                           rating=list(popular_df['avg_rating'].round(1).values)
                           )

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html', data=None, error=None)

@app.route('/recommend_books', methods=['POST'])
def recommend():
    user_input = request.form.get('user_input', '').strip()  # Get input and remove extra spaces

    # If the input is empty, redirect to the recommendation page
    if not user_input:
        return redirect(url_for('recommend_ui'))

    # Check if the book exists in the database
    if user_input not in pt.index:
        return render_template('recommend.html', data=None, error="Oops, we don't know that one.")

    # Get similar books
    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]

    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        data.append(item)

    return render_template('recommend.html', data=data, error=None)

if __name__ == '__main__':
    app.run(debug=True)
