import os
os.system('cls||clear')

# Code starts here

import time
import random

print("H A N G M A N\n")
clue = input('Type "play" to play the game, "exit" to quit:') 
words_list = ["python", "java", "kotlin", "javascript"]
word = list(random.choice(words_list))
guesses = list("-" * len(word))
print("".join(guesses))

count = 8
tried_letter = []
while (clue != "play") and (clue != "exit"):
    print("Invalid Input!Try again!")
    clue = input('Type "play" to play the game, "exit" to quit:')
if clue == "exit":
    print("You've quitted the game!See you next time!")
    exit()
if clue == "play":
    start_time = time.time()
    timeout = 30
    while count > 0:
        print()
        print("".join(guesses))

        time_left = (timeout - (time.time() - start_time))
        print(f"Time left: {time_left:.2f}")
        user_letter = input("Input a letter: ")
        if (time.time() - start_time) >= timeout:
            print("There is no time left. Try again next time!")
            exit()
        if len(user_letter) != 1:
            print("You should input a single letter")
            tried_letter.append(user_letter)
            continue
        elif not user_letter.islower() or not user_letter.isalpha():
            print("Please enter a lowercase English letter")
            tried_letter.append(user_letter)
            continue
        elif user_letter in guesses or user_letter in tried_letter:
            print("You've already guessed this letter")
            continue
        elif user_letter in word and user_letter not in guesses:
            for i in range(len(word)):
                if user_letter == word[i]:
                    guesses[i] = user_letter
                    if "-" not in guesses:
                        print("Congratulations! You guessed the word!")
                        print("You survived!")
                        exit()
        else:
            print("That letter doesn't appear in the word")
            tried_letter.append(user_letter)
            count -= 1
            if count == 0:
                print("You lost!Try again next time!")


