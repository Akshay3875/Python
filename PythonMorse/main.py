from flask import Flask, render_template, request

app = Flask(__name__)

# Morse Code Dictionary
MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                  'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                  'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                  'Y': '-.--', 'Z': '--..',
                  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
                  '8': '---..', '9': '----.', '0': '-----', ' ': '/'}

# Function to convert text to Morse code
def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + ' '
        else:
            morse_code += ' '
    return morse_code.strip()

# Function to convert Morse code to text
def morse_to_text(morse_code):
    text = ''
    morse_code = morse_code.split(' ')
    for code in morse_code:
        for key, value in MORSE_CODE_DICT.items():
            if code == value:
                text += key
    return text

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the form submission and conversion
@app.route('/convert', methods=['POST'])
def convert():
    user_input = request.form['user_input']
    choice = request.form['choice']

    # Perform the chosen conversion based on user input
    if choice == 'text_to_morse':
        result = text_to_morse(user_input)
    elif choice == 'morse_to_text':
        result = morse_to_text(user_input)
    else:
        result = 'Invalid choice'

    # Render the result on the HTML template
    return render_template('index.html', user_input=user_input, result=result)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
