from flask import Flask, request
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)  # allows JavaScript from another origin to access backend

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    name = data['name']
    email = data['email']
    message = data['message']

    try:
        connection = mysql.connector.connect(
            host='sql306.infinityfree.com',
            user='if0_39577314if0_39577314',
            password='VedantMali09',
            database='if0_39577314_poppiuox'
        )
        cursor = connection.cursor()
        query = "INSERT INTO form_data (name, email, message) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, email, message))
        connection.commit()
        return "Success"
    except Exception as e:
        print("Error:", e)
        return "Error", 500
