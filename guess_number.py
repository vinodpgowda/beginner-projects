import random

def guess_number(x):    
    random_number = random.randint(1,x)
    guess = False
    while(not guess):   
        number = int(input(f"\nGuess the secret number between 1 and {x}: "))
        if number == random_number:
            print(f"You guessed it correctly, the number is {random_number}")
            guess = True
        elif number < random_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    print(f"Guess your secret number which is between 1 and {x}")
    while (feedback != 'c'):
        number = (low+high)//2
        print(f"Computer guessed {number}")
        feedback = input("Feedback with (l) for lower, (h) for higher OR (c) for correct guess: ")
        if feedback == 'h':
            high = number - 1 
        elif feedback == 'l':
            low = number + 1
    print(f"Computer has guess your secret number {number}")

# guess(100)
computer_guess(100)
