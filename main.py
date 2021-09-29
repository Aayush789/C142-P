from flask import Flask , jsonify, request
import csv
from storage import all_articles,liked_articles,not_liked_articles
from demographic_filtering import output
from content_filtering import get_recommendations

app = Flask(__name__)

@app.route("/get-articles")

def get_articles():

    articles_data = {
        "title": all_articles[0][12],
    }
    return jsonify({
        "data": all_articles[0],
        "status": "success"
    })

@app.route("/liked-articles", methods = ["POST"])

def liked_articles():
    articles = all_articles[0]
    liked_articles.append(articles)
    all_articles.pop(0)
    return jsonify({
        "status": "success"
    }),201

@app.route("/unliked-articles", methods = ["POST"])

def unliked_articles():
    articles = all_articles[0]
    all_articles.pop(0)
    not_liked_articles.append(articles)
    return jsonify({
        "status": "success"
    }),201

if __name__ == "__main__":
    app.run()



