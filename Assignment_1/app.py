from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the API! Access /api to get the data."

@app.route('/api')
def get_data():
        # open the json file in read mode
    with open('data.json', 'r') as file:
        # convert the json file into python dictionary
       data = json.load(file)
        # convert python data into json response
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)