from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# Get MongoDB URI from .env
mongo_uri = os.getenv("MONGO_URI")

client = MongoClient(mongo_uri)
db = client["todoDB"]
collection = db["todos"]

@app.route("/")
def home():
    return "Flask backend running successfully"

@app.route("/submittodoitem", methods=["POST"])
def submit_todo():
    data = request.get_json()

    itemName = data.get("itemName")
    itemDescription = data.get("itemDescription")

    todo = {
        "itemName": itemName,
        "itemDescription": itemDescription
    }

    collection.insert_one(todo)

    return jsonify({"message": "Item saved successfully"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
