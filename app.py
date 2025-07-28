from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Connect to MySQL (edit these with your DB details)
conn = mysql.connector.connect(
    host="sql306.infinityfree.com",
    user="if0_39577314_poppiuox",
    password="VedantMali09",
    database="if0_39577314_user"
)
cursor = conn.cursor()

@app.route("/")
def form():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]
    
    cursor.execute("INSERT INTO form_data (name, email, message) VALUES (%s, %s, %s)", (name, email, message))
    conn.commit()
    
    return "Form submitted successfully!"

if __name__ == "__main__":
    app.run(debug=True)
