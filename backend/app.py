from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from bson.json_util import dumps
from dotenv import load_dotenv
import os

app = Flask(__name__)
CORS(app)

# Load MongoDB Atlas connection string from .env file
load_dotenv()
mongo_uri = os.getenv("MONGO_URI")

client = MongoClient(mongo_uri)

# Select the database and collection you want to use
db = client["movies_db"]
collection = db["movie"]

# ElasticSearch connection
es = Elasticsearch(os.getenv("ELASTIC_URI"))

@app.route('/', methods=['GET'])
def get_movies():
    # Get all documents from MongoDB
    documents = collection.find()
    response = dumps(documents)
    return response, 200

@app.route('/load_movies', methods=['GET'])
def load_movies():
    # Get all documents from MongoDB
    documents = collection.find()
    # Create index in ElasticSearch
    es.indices.create(index='movies_index', ignore=400)
    # Prepare data for bulk indexing
    bulk_data = []
    for document in documents:
        data = dumps(document)
        bulk_data.append({
            '_index': 'movies_index',
            '_id': document['_id'],
            '_source': data
        })
    # Bulk index data in ElasticSearch
    response = bulk(es, bulk_data)
    return jsonify({'message': f'{len(response)} documents indexed successfully'}), 200

# Insert document into MongoDB
@app.route('/insert_movies', methods=['POST'])
def insert_movies():
    data = request.json
    result = collection.insert_one(data)
    return jsonify({'message': 'Document inserted successfully', 'id': str(result.inserted_id)}), 200

# Search documents in ElasticSearch
@app.route('/search_movies', methods=['POST'])
def search_movies():
    data = request.json
    query = {
        "query": {
            "multi_match": {
                "query": data['query'],
                "fields": ["title^3", "description^2", "genre^2"]
            }
        }
    }
    result = es.search(index='movies_index', body=query)
    hits = result['hits']['hits']
    response = [{'id': hit['_id'], 'title': hit['_source']['title'], 'description': hit['_source']['description']} for hit in hits]
    return jsonify({'hits': response}), 200

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
