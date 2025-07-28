from flask import Flask, render_template, request
import sqlite3  # You can change to MySQL if needed

app = Flask(__name__)

# Home route - show the form
@app.route("/")
def form():
    return render_template("form.html")

# Handle form submission
@app.route("/submit", methods=["POST"])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Store in SQLite (or use your MySQL connection here)
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, email TEXT, message TEXT)")
    c.execute("INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)", (name, email, message))
    conn.commit()
    conn.close()

    return "Form submitted successfully!"

if __name__ == "__main__":
    app.run(debug=True)
