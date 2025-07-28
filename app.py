from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Connect to MySQL (update with Railway values)
conn = mysql.connector.connect(
    host="containers-us-west-197.railway.app",  # <-- Use your actual MYSQLHOST
    user="root",
    password="KKBBxFwvAsrIuEbSpcKbDEAaOenjbWfM",
    database="railway",
    port=7807  # <-- Use your actual MYSQLPORT (from Railway Variables)
)

cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS form_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    message TEXT
)
""")
conn.commit()

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
