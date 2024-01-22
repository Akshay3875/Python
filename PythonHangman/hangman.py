import random
from flask import Flask, render_template, request

app = Flask(__name__)

# List of words for the game
words = ["python", "hangman", "flask", "javascript", "html", "css", "code"]

# Select a random word from the list
chosen_word = random.choice(words)
guessed_word = ["_"] * len(chosen_word)
attempts_left = 6
game_over = False

@app.route('/')
def index():
    return render_template('index.html', guessed_word=guessed_word, attempts_left=attempts_left, game_over=game_over)

@app.route('/check_letter', methods=['POST'])
def check_letter():
    global attempts_left, game_over

    if not game_over:
        letter = request.form['letter']

        if letter not in chosen_word:
            attempts_left -= 1

        for i in range(len(chosen_word)):
            if chosen_word[i] == letter:
                guessed_word[i] = letter

        if "_" not in guessed_word:
            game_over = True

        if attempts_left == 0:
            game_over = True

    return render_template('index.html', guessed_word=guessed_word, attempts_left=attempts_left, game_over=game_over)

@app.route('/reset')
def reset():
    global chosen_word, guessed_word, attempts_left, game_over
    chosen_word = random.choice(words)
    guessed_word = ["_"] * len(chosen_word)
    attempts_left = 6
    game_over = False
    return render_template('index.html', guessed_word=guessed_word, attempts_left=attempts_left, game_over=game_over)


if __name__ == '__main__':
    app.run(debug=True)
