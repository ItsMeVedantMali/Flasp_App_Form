from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Flask app is running!"

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    name = data['name']
    email = data['email']
    message = data['message']

    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            database=os.getenv("DB_NAME")
        )
        cursor = connection.cursor()
        query = "INSERT INTO form_data (name, email, message) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, email, message))
        connection.commit()
        return "Success"
    except Exception as e:
        print("Error:", e)
        return "Error", 500
