from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Connect to MySQL (edit these with your DB details)
conn = mysql.connector.connect(
    host="mysql.railway.internal",
    user="root",
    password="AamhysZuwcXpiIekuJCjaNkTaiXQwPlQ",
    database="railway"
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
