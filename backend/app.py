from flask import Flask, jsonify, request
from pymongo import MongoClient

# Replace <username>, <password>, <cluster-name>, and <dbname> with your credentials
client = MongoClient("mongodb+srv://bigdata:<97vfrvSnTdySjEJf>@cluster0.aj9bqer.mongodb.net/?retryWrites=true&w=majority")
# db = client.test

db = client["Books"]
collection = db["book"]

app = Flask(__name__)

@app.route("/all-books")
def get_books():
    documents = collection.find()

    result = []
    for doc in documents:
        result.append(doc)
    
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
