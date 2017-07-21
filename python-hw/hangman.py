import random

attempts = 6
guesses = []
wins = 0
losses = 0
money = 50
player = True
words = ['bird','ape','parrot','cat','kangaroo']

while player == True  or money > 0:
    word = random.choice(words)
    print(f'you have ${money} \nguesses left: {attempts}')
    print('_ ' * len(word))
    while attempts > 0 and money > 0:
        letter = input("Guess a letter.")
        if letter in word:
            money += 5
            print("You got it! \n \n \n" + "_" * 16)
            print('_ ' * len(word))
            print(f'you have ${money} \nguesses left: {attempts}')
        elif letter in guesses:
            print("You've already guessed this letter")
        else:
            money -= 5
            attempts -= 1
            guesses.append(letter)
            print("You did not get it \n \n \n" + "_" * 16)
            print('_ ' * len(word))
            print(f'you have ${money} \nguesses left: {attempts}')
            print(guesses)

    play_again = input("would you like to play again? y/n")
    if play_again == "y":
        continue
    elif play_again == "n":
        break
    else:
        print("enter y or n")





