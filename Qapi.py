# from fastapi import FastAPI, HTTPException,Query
# import pymongo

# app = FastAPI()

# AccessMongo = pymongo.MongoClient("mongodb://localhost:27017/")
# Qdatabase = AccessMongo["Questions_api"]
# Qcollections = Qdatabase["Questions"]

# @app.get('/api/AllQuestions',methods=['GET'])
# def get_AllQuestions():
#     AllDocs = list(Qcollections.find())

#     data = {'Questions':AllDocs}
#     json_convert = data.to_dict(orient="records")
#     return json_convert


from flask import Flask, jsonify, render_template, request
from pymongo import MongoClient
from bson import ObjectId, json_util

app = Flask(__name__)

# Replace the connection string with your MongoDB connection string
uri = 'mongodb://localhost:27017/'
database_name = 'Questions_api'

# Create a MongoDB client
client = MongoClient(uri)

def connect_to_database():
    return client[database_name]

@app.route('/api/questions', methods=['GET'])
def get_questions():
    try:
        # Connect to the MongoDB server
        db = connect_to_database()
        print('Connected to the database')

        # Access the "Questions" collection
        questions_collection = db['Questions']

        # Retrieve all documents in the "Questions" collection
        documents = list(questions_collection.find())

        # Format the data to send as JSON using json_util
        data = {'Questions': json_util.dumps(documents)}
        
        return jsonify(data) 

    finally:
        # Close the MongoDB connection
        client.close()
        print('Connection closed')

@app.route('/api/questions/<question_id>', methods=['GET'])
def get_question_by_id(question_id):
    try:
        # Connect to the MongoDB server
        db = connect_to_database()
        print('Connected to the database')

        # Access the "Questions" collection
        questions_collection = db['Questions']

        # Retrieve a specific document by ID
        document = questions_collection.find_one({'_id': ObjectId(question_id)})

        if document:
            # Format the data to send as JSON using json_util
            return jsonify(json_util.dumps(document))
        else:
            return jsonify({'error': 'Question not found'}), 404

    finally:
        # Close the MongoDB connection
        client.close()
        print('Connection closed')

@app.route('/api/questions', methods=['POST'])
def add_question():
    try:
        # Connect to the MongoDB server
        db = connect_to_database()
        print('Connected to the database')

        # Access the "Questions" collection
        questions_collection = db['Questions']

        # Get data from the request
        data = request.json

        # Insert a new question into the "Questions" collection
        insert_result = questions_collection.insert_one(data)

        return jsonify({'message': 'Question added successfully', 'inserted_id': str(insert_result.inserted_id)})

    finally:
        # Close the MongoDB connection
        client.close()
        print('Connection closed')

if __name__ == '__main__':
    app.run(debug=True)
