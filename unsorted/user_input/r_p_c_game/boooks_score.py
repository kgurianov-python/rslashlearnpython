total = 0

repeat = int(input("Enter 1 to keep going or any other number to quit: "))
while repeat == 1:
    name = input("Enter name: ")
    books = int(input("Enter amount of books purchased this month: "))
    if books <= 0:
        user_score = 0
    elif books <= 2:
        user_score = 5
    elif books <= 4:
        user_score = 10
    elif books <= 5:
        user_score = 15
    elif books <= 7:
        user_score = 20
    elif books > 8:
        user_score = 25
    else:
        user_score = 0

    total += user_score
    print(f"{name} earned {user_score} this month")

    repeat = int(input("Enter 1 to keep going or any other number to quit: "))

print(f"Total score for all users is: {total}")
