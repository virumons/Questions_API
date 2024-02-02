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

from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

# Replace the connection string with your MongoDB connection string
uri = 'mongodb://localhost:27017/'
database_name = 'Questions_api'

# Create a MongoDB client
client = MongoClient(uri)

@app.route('/api/get_questions', methods=['GET'])
def get_questions():
    try:
        # Connect to the MongoDB server
        db = client[database_name]
        print('Connected to the database')

        # Access the "questions" collection
        questions_collection = db['Questions']

        # Retrieve all documents in the "questions" collection
        documents = list(questions_collection.find())

        # Format the data to send as JSON
        data = {'questions': documents}

        return jsonify(data)

    finally:
        # Close the MongoDB connection
        client.close()
        print('Connection closed')

if __name__ == '__main__':
    app.run(debug=True)
