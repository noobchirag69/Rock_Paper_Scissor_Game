import random

def validate(hand):
    if hand < 0 or hand > 2:
        return False
    return True

def print_hand(hand, name = 'Guest'):
    hands = ['Rock', 'Paper', 'Scissor']
    print(name + ' picked: ' + hands[hand])

#Define the judge function
def judge(player, computer):
    #Add control flow based on the comparison of player and computer
    if player == computer:
        return 'It is a tie! Try Again!!'
    elif player == 0 and computer == 1:
        return 'You loose! Better luck next time!'
    elif player == 1 and computer == 2:
        return 'You loose! Better luck next time!'
    elif player == 2 and computer == 0:
        return 'You loose! Better luck next time!'
    else:
        return 'Congratulations! You have won!!'

print('---Starting the Rock-Paper-Scissor Game---')
player_name = input('Please enter your name: ')

print('Pick a hand: (0: Rock, 1: Paper, 2: Scissor)')
player_hand = int(input('Please enter a number between 0 and 2: '))

if validate(player_hand):
    computer_hand = random.randint(0,2)

    print_hand(player_hand, player_name)
    print_hand(computer_hand, 'Computer')

    #Assign the return value of judge to the result variable
    result = judge(player_hand, computer_hand)
    #Print the result variable
    print('Result: ' + result)
else:
    print('Please enter a valid number.')
