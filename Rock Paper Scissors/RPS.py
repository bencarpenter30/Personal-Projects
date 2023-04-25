import random

# Building the armoury and setting the score counter
weapon_list = ['rock', 'paper', 'scissors']
score = [0,0,0]

# User selects their weapon
def get_user_weapon():
    while True:
        print('Rock, Paper or Scissors?')
        weapon = input()
        weapon = weapon.lower()
        valid = False
        for i in range(3):
            if weapon == weapon_list[i]:
                valid = True
        if valid == False:
            print('Invalid input. Please choose a valid weapon.\n')
        else:
            break
    return weapon

# Computer selects their weapon
def get_comp_weapon():
    number = random.randrange(0,3)
    weapon = weapon_list[number]
    return weapon

# Deciding the winner
def determine_winner(user,comp):
    if user == comp:    
        score[1] = score[1] + 1
        return 'You both chose ' + user + ". It's a draw"
    else:
        if user == 'rock':
            if comp == 'scissors':
                score[0] = score[0] + 1
                return 'Rock smashes scissors. You win!'
            else:
                score[2] = score[2] + 1
                return 'Paper covers rock. You lose.'
        elif user == 'scissors':
            if comp == 'paper':
                score[0] = score[0] + 1
                return 'Scissors cuts paper. You win!'
            else:
                score[2] = score[2] + 1
                return 'Rock smashes scissors. You lose.'
        else:
            if comp == 'rock':
                score[0] = score[0] + 1
                return 'Paper covers rock. You win!'
            else:
                score[2] = score[2] + 1
                return 'Scissors cuts paper. You lose.'

# Asking the user if they want to play again
def play_again():
    while True:
        print('Would you like to play again?')
        answer = input()
        answer = answer.lower()
        if answer != 'yes' and answer != 'no':
            print('Invalid input. Please try again.\n')
        elif answer == 'no':
            print('Thank you for playing.\n')
            quit()
        else:
            break
        
# The main function
def rps():
    while True:
        user_weapon = get_user_weapon()
        comp_weapon = get_comp_weapon()
        print('You chose ' + user_weapon + '.')
        print('The computer chose ' + comp_weapon + '.')
        msg = determine_winner(user_weapon,comp_weapon)
        print(msg + '\n')
        print('Score \nWins - ' + str(score[0]) + '\nDraws - ' + str(score[1]) + '\nLoses - ' + str(score[2]) + '\n')
        play_again()
        print('You have chosen to play again.\n')

print(rps())