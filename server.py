from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# Open the JSON file and read its contents
with open('db.json') as json_file:
    data = json.load(json_file)

# Define a GET endpoint to retrieve data from the JSON file
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(data)

# Define a POST endpoint to add data to the JSON file
@app.route('/students', methods=['POST'])
def add_student():
    # Get the data from the request body
    new_student = request.get_json()
    # Append the new data to the existing JSON file
    data['students'].append(new_student)
    # Open the JSON file and write the updated data
    with open('db.json', 'w') as json_file:
        json.dump(data, json_file)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
