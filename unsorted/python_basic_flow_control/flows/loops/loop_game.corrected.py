import random

CONTINUE = ('yes', 'y')
QUESTIONS = {"When did World War 1 begin?": "1914",
             "When were the Olympic games held in Berlin?": "1936",
             "What is the capital of Thailand?": "Bangkok",
             "When was the german reunification?": "1990",
             "What are the three primary colours?": "red, yellow, blue"}


# QUESTIONS_ADV = {"When did World War 1 begin?": ("1914",),
#                  "When were the Olympic games held in Berlin?": ("1936",),
#                  "What is the capital of Thailand?": ("Bangkok",),
#                  "When was the german reunification?": ("1990",),
#                  "What are the three primary colours?": ("red", "yellow", "blue")}


def main():
    d = {1: 'one', 3: 'three', 5: 'five', 'question': 'answer'}
    name = input("Enter your name:\t")
    print(f"Hello, {name},you will now take a quiz to test your intelligence!")
    print("You will answer a few questions and then be presented with your final score.")

    while (answer := input(f'Would you like to play a game? (yes/no)\t')).lower() in CONTINUE:
        score = 0
        keys = list(QUESTIONS.keys())
        random.shuffle(keys)
        for key in keys:
            answer = input(f'\t{key}\t')
            if answer.lower() == QUESTIONS[key].lower():
                print('Correct')
                score += 10
            else:
                print('Wrong! Go back to school!')
            print(f'Your current score: {score}')
        print(f'Your total score: {score}')


if __name__ == '__main__':
    main()
