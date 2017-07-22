import random
import string
attempts = 6
wrong_guesses = []
right_guesses = []
wins = 0
losses = 0
money = 50
player = True
words = ['bird', 'ape', 'parrot', 'cat', 'kangaroo']

# @TODO: move prints into separate function

# @TODO: check for wins and losses
while player == True or money > 0 or guessed != word:
    word = random.choice(words)
    # @TODO: use joint function to print out right letters
    guessed = " ".join(c if c in right_guesses else "_" for c in word)
    print(f'you have ${money} \nguesses left: {attempts}')
    print('_ ' * len(word))
    if guessed != word:
        while attempts > 0 and money > 0:
            letter = input("Guess a letter.")
            if letter in word:
                money += 5
                right_guesses.append(letter)
                print("You got it! \n \n \n" + "_" * 16)
                print(guessed)
                print(f'you have ${money} \nguesses left: {attempts}')
                print(wrong_guesses)
            elif letter in wrong_guesses or right_guesses:
                print("You've already guessed this letter")
                print(guessed)
                print(f'you have ${money} \nguesses left: {attempts}')
                print(wrong_guesses)
            elif len(letter) > 1:
                print("You can only guess one letter at a time")
                print(guessed)
                print(f'you have ${money} \nguesses left: {attempts}')
                print(wrong_guesses)
            elif letter.isalpha() == False:
                print("Dude, use an alphabet")
                print(guessed)
                print(f'you have ${money} \nguesses left: {attempts}')
                print(wrong_guesses)
            else:
                money -= 5
                attempts -= 1
                wrong_guesses.append(letter)
                print("You did not get it \n \n \n" + "_" * 16)
                print(guessed)
                print(f'you have ${money} \nguesses left: {attempts}')
                print(wrong_guesses)

    elif money == 0:
        print("You lost")
        break
    else:
        play_again = input("would you like to play again? y/n")
        # @TODO: find a way to continue loop after answer is Y
        if play_again == "n":
            break
        elif play_again == "y":
            player = True
        else:
            print("enter y or n")




