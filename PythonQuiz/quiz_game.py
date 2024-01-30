print("Welcome to the quiz game")

playing = input("Do you want to play the game? (y/n) ")

if playing != "y":
    quit()
    
print("Let's play a game")
score = 0

answer = input("What does CPU Stands for? ")
if answer == "Central Processing Unit":
    print("Correct")
    score += 1
else:
    print("Wrong")

answer = input("What does RAM stands for? ")
if answer == "Random Access Memory":
    print("Correct")
    score += 1
else:
    print("Wrong")

answer = input("What does HDD stands for? ")
if answer == "Hard Disk Drive":
    print("Correct")
    score += 1
else:
    print("Wrong")

answer = input("What does SSD stands for? ")
if answer == "Solid State Drive":
    print("Correct")
    score += 1
else:
    print("Wrong")

print("You scored " + str(score) + " out of 4")
print("You got " + str(int(score / 4 * 100)) + "%")
print("Thank you for playing")