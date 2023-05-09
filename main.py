import csv

from flask import Flask, jsonify, request

all_articles = []
liked_articles = []
disliked_articles = []

with open("shared_articles.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

app = Flask(__name__)

@app.route("/all-articles")
def get_articles():
    return jsonify({
        "data": all_articles[0],
        "message": "success"
    })

@app.route("/liked-article", methods = ["POST"])
def liked_article():
    article = all_articles[0]
    liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "message": "success"
    }), 201

@app.route("/disliked-article", methods = ["POST"])
def disliked_article():
    article = all_articles[0]
    disliked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "message": "success"
    }), 201

if(__name__ == "__main__"):
    app.run()
