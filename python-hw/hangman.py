import random

attempts = 6
guesses = []
wins = 0
losses = 0
money = 50
player = True
words = ['bird','ape','parrot','cat','kangaroo']

while player == True or (attempts > 0 and money > 0):
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
        else:
            money -= 5
            attempts -= 1
            print("You did not get it \n \n \n" + "_" * 16)
            print('_ ' * len(word))
            print(f'you have ${money} \nguesses left: {attempts}')
            print(guesses.append(letter))


