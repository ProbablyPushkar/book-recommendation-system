# 📚 Book Recommender System

A Flask-based web app that recommends books based on user input using collaborative filtering.

## 🚀 Features

- Recommends similar books based on user selection
- Displays book title, author, and cover image
- Built with Flask and rendered via HTML templates
- Uses pre-processed data for fast recommendation

## 🗂 Project Structure

├── app.py # Flask application
├── templates/
│ ├── index.html # Homepage with popular books
│ └── recommend.html # Recommendation page
├── books.pkl # Book metadata
├── popular.pkl # Pre-computed popular books
├── pt.pkl # Pivot table
├── similarity_scores.pkl # Similarity matrix for recommendations
├── book-recommender-system.ipynb # Jupyter notebook for model dev
└── README.md # Project documentation


## 🛠 Requirements

- Python 3.x
- Flask
- NumPy
- Pandas
- Jupyter (for notebook)

📁 Large Files

Some necessary files are hosted externally due to GitHub file size limitations:

- [books.pkl (70MB)](https://drive.google.com/uc?export=download&id=16nuuFdnTyfNYZpWT10X96hkAQCk8uwcu)


Install dependencies:
```bash
pip install flask numpy pandas
