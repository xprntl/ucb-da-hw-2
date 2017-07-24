import random

wins = 0
losses = 0
money = 50
player = True
words = ['bird', 'ape', 'parrot', 'cat', 'kangaroo']

while player:
    word = random.choice(words)
    attempts = 7
    wrong_guesses = []
    right_guesses = []
    guessed_word = ""
    print('_ ' * len(word))
    while attempts > 0 and money > 0 and guessed_word.replace(" ", "") != word:
        letter = input("Guess a letter.")
        if letter in word:
            money += 5
            right_guesses.append(letter)
            print("You got it! \n \n \n" + "_" * 16)
        elif letter in wrong_guesses:
            print("You've already guessed this letter")
        elif len(letter) > 1:
            print("You can only guess one letter at a time")
        elif letter.isalpha() == False:
            print("Dude, use the alphabet")
        else:
            money -= 5
            attempts -= 1
            wrong_guesses.append(letter)
            print("You did not get it \n \n \n" + "_" * 16)

        guessed_word = " ".join(letter if letter in right_guesses else "_ " for letter in word)
        print(guessed_word)
        print(f'you have ${money} \nguesses left: {attempts}')
        print(wrong_guesses)

    if ( guessed_word.replace(" ", "") == word):
        wins = wins + 1
    else:
        losses = losses + 1

    print("your wins: " + str(wins))
    print("your losses: " + str(losses))
    player = input("do you want to play again? y or n.") == "y"