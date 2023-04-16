from flask import Flask, jsonify

app = Flask(__name__)

movies = [
    {"title": "The Shawshank Redemption", "year": 1994, "director": "Frank Darabont"},
    {"title": "The Godfather", "year": 1972, "director": "Francis Ford Coppola"},
    {"title": "The Godfather: Part II", "year": 1974, "director": "Francis Ford Coppola"},
    {"title": "The Dark Knight", "year": 2008, "director": "Christopher Nolan"},
    {"title": "12 Angry Men", "year": 1957, "director": "Sidney Lumet"},
]

@app.route('/movies')
def get_movies():
    return jsonify(movies)
