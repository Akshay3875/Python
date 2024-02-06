import random
import time

def generate_sentance():
    sentences = [
        "My name is Akshay."
        "A week has seven days."
    ]
    return random.choice(sentences)

def typing_speed_test():
    print("Welcome to the Typing Speed Test!")
    input("Press Enter when you are ready to start...")

    sentence = generate_sentance()
    print(f"\nType the following sentence:\n\n{sentence}\n")

    start_time = time.time()
    user_input = input("Your typing: ")
    end_time = time.time()

    elapsed_time = end_time - start_time
    words_per_minute = (len(sentence.split()) / elapsed_time) * 60

    print("\nTyping Speed Results:")
    print(f"Time taken: {elapsed_time:.2f} seconds")
    print(f"Words per minute: {words_per_minute:.2f} WPM")

if __name__ == "__main__":
    typing_speed_test()
