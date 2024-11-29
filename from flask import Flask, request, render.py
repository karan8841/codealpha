from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# Database connection
def get_db():
    conn = sqlite3.connect('user_data.db')
    return conn

@app.route('/')
def home():
    return render_template_string("""
        <form method="POST" action="/submit">
            Name: <input type="text" name="name"><br>
            Age: <input type="number" name="age"><br>
            <input type="submit" value="Submit">
        </form>
    """)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    age = request.form['age']

    # Storing user input directly in the database
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()

    return f"Hello {name}, your age is {age}!"

if __name__ == '__main__':
    app.run(debug=True)
