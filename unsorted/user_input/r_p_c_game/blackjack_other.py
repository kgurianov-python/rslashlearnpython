import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
rand_card = random.choice(cards)
player_cards = []
computer_cards = []

def deal():
    return random.choice(cards)

def deal_player():
    for _ in range(2):
        card = deal()
        player_cards.append(card)

def deal_computer():
    for _ in range(2):
        card = deal()
        computer_cards.append(card)

def calculate_score(list):
    score = sum(list)
    if len(list) < 3 and score == 21:
        return 0
    if 11 in list and score > 21:
        list.remove(11)
        list.append(1)
        score = sum(list)
    return score

def blackjack():
    deal_player()
    deal_computer()
    playing = True

    while playing:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        playing = player_score and computer_score
        player_report = f"Your cards: {player_cards}. Your score is {player_score}."
        computer_init_report = f"Computer's first card: {computer_cards[0]}."
        print(player_report)
        print(computer_init_report)
        print(computer_cards)

        prompt = input('Type "y" to get another card or "n" to pass: ')
        if prompt == 'y':
            deal()
            new_card = deal()
            player_cards.append(new_card)
            player_score = calculate_score(player_cards)
            player_report = f"Your cards: {player_cards}. Your score is {player_score}"
            print(player_report)
            print(computer_init_report)
            print(f"Player score is {player_score}")
        elif prompt == 'n':
            playing = False

        if player_score == 0:
            print("Finishing the game")
            playing = False
        elif player_score > 21:
            print("Finishing the game")
            playing = False

        print(f"{playing=}")

        while computer_score < 17:
            deal()
            new_computer_card = deal()
            computer_cards.append(new_computer_card)
            computer_score = calculate_score(computer_cards)
        computer_report = f"Computer's cards: {computer_cards}. Computer's score is {computer_score}."

        print(player_report)
        print(computer_report)
        if player_score == 21:
            print('You win with 21.')
        elif computer_score == 21:
            print('Computer wins with 21.')
        elif player_score > 21:
            print(f"You bust! Computer wins with {computer_score}.")
        elif computer_score > 21:
            print(f"Computer busts! You win with {player_score}")
        elif player_score > computer_score:
            print(
                f"You win with {player_score} over computer's score of {computer_score}."
            )
        elif computer_score > player_score:
            print(
                f"Computer wins with {computer_score} over your score of {player_score}."
            )
        elif computer_score == player_score:
            print("It's a draw! Play again!")

if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y': blackjack()