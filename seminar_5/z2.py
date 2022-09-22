import random

def check_digit(text):
    while True:
        try:
            input_text = input(text)
            if input_text.isdigit():
                input_text = int(input_text)
                break
        except ValueError:
            print('Error! Not a number!')
    return input_text

def player(count_candies, turn):
    while True:
        player_turn = check_digit(f'Input number from 1 to {turn}: ')

        if player_turn <= turn and player_turn > 0:
            break
    
    count_candies -= player_turn

    return count_candies

def bot(count_candies, turn):
    if count_candies < turn:
        turn = turn - (turn - count_candies) - 1
    
    count_candies -= turn

    return count_candies

def vsplayer(count_candies, turn):
    who_first = bool(random.choice([True, False]))

    while count_candies > 1:
        if who_first == True:
            print(f'First player turn. Count of candies is {count_candies}')
            count_candies = player(count_candies, turn)

            if count_candies > 0:
                who_first = False
        
        if who_first == False:
            print(f'Second player turn. Count of candies is {count_candies}')
            count_candies = player(count_candies, turn)

            if count_candies > 0:
                who_first = True
        
        if count_candies < turn:
            turn = turn - (turn - count_candies)

    print(f'Left {count_candies} candies')

    if who_first == True:
        print('Player 1, u lost!')
    if who_first == False:
        print('Player 2, u lost!')

def vsbot(count_candies, turn):
    who_first = bool(random.choice([True, False]))

    while count_candies > 1:
        if who_first == True:
            print(f'First player turn. Count of candies is {count_candies}')
            count_candies = player(count_candies, turn)

            if count_candies > 0:
                who_first = False
        
        if who_first == False:
            print(f'Bot turn. Count of candies is {count_candies}')
            count_candies = bot(count_candies, turn)

            if count_candies > 0:
                who_first = True
        
        if count_candies < turn:
            turn = turn - (turn - count_candies)

    print(f'Left {count_candies} candies')

    if who_first == True:
        print('Player 1, u lost!')
    if who_first == False:
        print('Bot lost!')

count_candies = check_digit('Input count of candys - ')

while True:
    count_candies_per_turn = check_digit('Input count candys per turn - ')
    if count_candies_per_turn < count_candies:
        break
    
while True:
    bot_or_player = check_digit('If u want to play vs "bot", input 1. If u want play vs "player", input 2 - ')
    if bot_or_player == 1:
        vsbot(count_candies, count_candies_per_turn)
        break
    elif bot_or_player == 2:
        vsplayer(count_candies, count_candies_per_turn)
        break
    else:
        print('Input 1 or 2')





