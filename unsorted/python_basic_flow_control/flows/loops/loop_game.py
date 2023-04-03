import random

# Here I am creating a loop, everything in-between the loop is indented
score = 0
name = input("Enter your name: ")
print("\n")
print("Hello",name,"you will now take a quiz to test your intelligence")
print("\n")
print("You will answer a few questions and then be presented with your final score ")
print("\n")

code="yes"
while code == "yes" or code == "Yes":
    ready = input("Are you ready, yes or no? ")

    # I have used variables for the two different players
    if ready == "yes" or ready == "Yes":
        print("\n")
        print ("Ok let's begin")
    elif ready == "no" or ready == "No":
        print("\n")
        break
    else:
        print("\n")
        print("???")
        print("\n")
        break

    # I created an if statement to ask if the person wants to play the game
    print("\n")
    print("Your first question is: ")
    print("\n")
    Questions = ["When did World War 1 begin? ", "When were the Olympic games held in Berlin? ", "What is the capital of Thailand? ", "When was the german reunification? ", "What are the three primary colours? "]
    Question1 = random.choice(Questions)
    Answer1 = input(Question1)
    if Answer1 == "1990" or Answer1 == "Bangkok" or Answer1 == "1914" or Answer1 == "1936" or Answer1 == "Red, Yellow, Blue" or Answer1 == "red, yellow, blue" or Answer1 == "Red, Blue, Yellow" or Answer1 == "red, blue, yellow" or Answer1 == "Yellow, Blue, Red" or Answer1 == "yellow, blue, red" or Answer1 == "Yellow, Red, Blue" or Answer1 == "yellow, red, blue" or Answer1 == "Blue, Yellow, Red" or Answer1 == "blue, yellow, red" or Answer1 == "Blue, Red, Yellow" or Answer1 == "blue, red, yellow":
        print("\n")
        print("Correct!")
        print("\n")
        Questions.remove(Question1)
        score = score + 10
        print("Your score is", score)
    else:
        print("\n")
        print("I'm sorry, that's not right")
        print("\n")
        Questions.remove(Question1)
        print("Your score is", score)

    print("\n")
    print("Alright, next question")
    print("\n")

    Question2 = random.choice(Questions)
    Answer2 = input(Question2)
    if Answer2 == "1990" or Answer2 == "Bangkok" or Answer2 == "1914" or Answer2 == "1936" or Answer2 == "Red, Yellow, Blue" or Answer2 == "red, yellow, blue" or Answer2 == "Red, Blue, Yellow" or Answer2 == "red, blue, yellow" or Answer2 == "Yellow, Blue, Red" or Answer2 == "yellow, blue, red" or Answer2 == "Yellow, Red, Blue" or Answer2 == "yellow, red, blue" or Answer2 == "Blue, Yellow, Red" or Answer2 == "blue, yellow, red" or Answer2 == "Blue, Red, Yellow" or Answer2 == "blue, red, yellow":
        print("\n")
        print("Correct!")
        print("\n")
        Questions.remove(Question2)
        score = score + 10
        print("Your score is", score)
    else:
        print("\n")
        print("I'm sorry, that's not right")
        print("\n")
        Questions.remove(Question2)
        print("Your score is", score)

    print("\n")
    print("Ok, next question")
    print("\n")

    Question3 = random.choice(Questions)
    Answer3 = input(Question3)
    if Answer3 == "1990" or Answer3 == "Bangkok" or Answer3 == "1914" or Answer3 == "1936" or Answer3 == "Red, Yellow, Blue" or Answer3 == "red, yellow, blue" or Answer3 == "Red, Blue, Yellow" or Answer3 == "red, blue, yellow" or Answer3 == "Yellow, Blue, Red" or Answer3 == "yellow, blue, red" or Answer3 == "Yellow, Red, Blue" or Answer3 == "yellow, red, blue" or Answer3 == "Blue, Yellow, Red" or Answer3 == "blue, yellow, red" or Answer3 == "Blue, Red, Yellow" or Answer3 == "blue, red, yellow":
        print("\n")
        print("Correct!")
        print("\n")
        Questions.remove(Question3)
        score = score + 10
        print("Your score is", score)
    else:
        print("\n")
        print("I'm sorry, that's not right")
        print("\n")
        Questions.remove(Question3)
        print("Your score is", score)

    print("\n")
    print("Ok, next question")
    print("\n")

    Question4 = random.choice(Questions)
    Answer4 = input(Question4)
    if Answer4 == "1990" or Answer4 == "Bangkok" or Answer4 == "1914" or Answer4 == "1936" or Answer4 == "Red, Yellow, Blue" or Answer4 == "red, yellow, blue" or Answer4 == "Red, Blue, Yellow" or Answer4 == "red, blue, yellow" or Answer4 == "Yellow, Blue, Red" or Answer4 == "yellow, blue, red" or Answer4 == "Yellow, Red, Blue" or Answer4 == "yellow, red, blue" or Answer4 == "Blue, Yellow, Red" or Answer4 == "blue, yellow, red" or Answer4 == "Blue, Red, Yellow" or Answer4 == "blue, red, yellow":
        print("\n")
        print("Correct!")
        print("\n")
        Questions.remove(Question4)
        score = score + 10
        print("Your score is", score)
    else:
        print("\n")
        print("I'm sorry, that's not right")
        print("\n")
        Questions.remove(Question4)
        print("Your score is", score)

    print("\n")
    print("Ok, next question")
    print("\n")

    Question5 = random.choice(Questions)
    Answer5 = input(Question5)
    if Answer5 == "1990" or Answer5 == "Bangkok" or Answer5 == "1914" or Answer5 == "1936" or Answer5 == "Red, Yellow, Blue" or Answer5 == "red, yellow, blue" or Answer5 == "Red, Blue, Yellow" or Answer5 == "red, blue, yellow" or Answer5 == "Yellow, Blue, Red" or Answer5 == "yellow, blue, red" or Answer5 == "Yellow, Red, Blue" or Answer5 == "yellow, red, blue" or Answer5 == "Blue, Yellow, Red" or Answer5 == "blue, yellow, red" or Answer5 == "Blue, Red, Yellow" or Answer5 == "blue, red, yellow":
        print("\n")
        print("Correct!")
        print("\n")
        Questions.remove(Question5)
        score = score + 10
    else:
        print("\n")
        print("I'm sorry, that's not right")
        print("\n")
        Questions.remove(Question5)

    print("Ok, that was the last question. Your final score is", score)
    print("\n")
    code = input("Would you like to try again, yes or no? ")
    print("\n")

print("See you later then, bye")