# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for

# Create a Flask web application
app = Flask(__name__)

# Dummy data for user registration (replace with a database in a real-world application)
users = []

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Simple validation (you should implement more robust validation in a real application)
        if not username or not password:
            return render_template('register.html', error='All fields are required')

        # Check if the username is already taken
        if any(user['username'] == username for user in users):
            return render_template('register.html', error='Username already taken')

        # Add the user to the list (in a real-world application, this should go to a database)
        users.append({'username': username, 'password': password})

        return redirect(url_for('login'))

    return render_template('register.html', error=None)

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Simple authentication (you should implement proper authentication in a real application)
        if any(user['username'] == username and user['password'] == password for user in users):
            return f'Hello, {username}! You are now logged in.'
        else:
            return render_template('login.html', error='Invalid username or password')

    return render_template('login.html', error=None)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
