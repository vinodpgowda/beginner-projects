import random

def play():
    user = input("\nRock Papers Scissors!!!\nSelect 'r' for Rock, 'p' for Paper, 's' for scissors: ")
    computer = random.choice(['r','p','s'])
    print(f'\nUser chose {user} and computer chose {computer}\n')
    if (user == computer):
        return "It's Tie\n"
    
    if (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p'):
        return "You won!\n"

    return "You lost!\n"

print(play())
