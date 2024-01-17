from flask import Flask, render_template, request
import random

app = Flask(__name__)
secret_number = random.randint(1, 100)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/guess", methods=["POST"])
def guess():
    user_guess = int(request.form["guess"])

    if user_guess == secret_number:
        result = "Congratulations! You guessed the correct number."
    elif user_guess < secret_number:
        result = "Too low. Try again!"
    else:
        result = "Too high. Try again!"

    return render_template("result.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
