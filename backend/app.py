from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from elasticsearch.helpers.errors import BulkIndexError
from bson.json_util import dumps, loads
from dotenv import load_dotenv
import os

app = Flask(__name__)
CORS(app)

# Load MongoDB Atlas connection string from .env file
load_dotenv()
mongo_uri = os.getenv("MONGO_URI")

client = MongoClient(mongo_uri)

# Select the database and collection you want to use
db = client["author_db"]
collection = db["authors"]

# ElasticSearch connection
es = Elasticsearch(os.getenv("ELASTIC_URI"), api_key=os.getenv("ELASTIC_API_KEY"))


@app.route("/enter_authors", methods=["GET"])
def get_movies():
    # Get all documents from MongoDB
    documents = [
        {"name": "Aayush Lamichhane", "roll": "075BCT004"},
        {"name": "Aayush Neupane", "roll": "075BCT006"},
        {"name": "Ankit Paudel", "roll": "075BCT013"},
        {"name": "Ashish Lamsal", "roll": "075BCT016"},
    ]

    # Insert the document into the collection
    result = collection.insert_many(documents)
    return jsonify({"message": "Data inserted successfully"})


def get_data(data):
    data["_id"] = str(data["_id"])
    return data


@app.route("/load_authors", methods=["GET"])
def load_movies():
    # Get all documents from MongoDB
    documents = collection.find()
    return jsonify({"message": [get_data(doc) for doc in documents]})


# Search documents in ElasticSearch
@app.route("/search_articles", methods=["POST"])
def search_articles():
    data = request.json
    query = {
        "query": {
            "multi_match": {
                "query": data["query"],
            }
        }
    }
    result = es.search(body=query)
    hits = result["hits"]["hits"]
    response = [
        {
            "id": hit["_id"],
            "title": hit["_source"]["headline"],
            "description": hit["_source"]["short_description"],
            "link": hit["_source"]["link"],
        }
        for hit in hits
    ]
    return jsonify({"hits": response}), 200


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)
