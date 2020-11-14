# 1. In the main menu, a player can choose to either play or exit the game. DONE
# 2. If the user chooses to play, the computer picks a word from a list: this will be the answer to the puzzle. DONE
# 3. The computer asks the player to enter a letter that they think is in the word. DONE
# 4.If that letter does not appear in the word and this letter hasn't already been guessed,
# the computer counts it as a miss. A player can only afford 8 misses before the game is over. DONE
# 5. If the letter does occur in the word, the computer notifies the player. If there are letters left to guess,
# the computer invites the player to go on. DONE
# 6. When the entire word is uncovered, it's a victory! DONE
# The game calculates the final score and returns to the main menu.
import random


def hint(word, guess_letters):
    result = ''
    for i in word:
        if i in guess_letters:
            result += i
        else:
            result += '-'
    return result


def start_game():
    print("New game")
    words = "python", "java", "kotlin", "javascript"
    word = random.choice(words)
    word_set = set(word)
    guess_letters = set()
    used_letters = set()
    attempts = 8
    while attempts != 0 and guess_letters != word_set:
        print(hint(word, guess_letters))
        guess = input("Input a letter: ")
        if guess in used_letters:
            print("You've already guessed this letter")
        else:
            if guess in word_set:  # letter in word
                used_letters.add(guess)
                guess_letters.add(guess)
            elif len(guess) != 1:
                print("You should input a single letter")
            elif not (guess.isalpha() and guess.islower()):
                print("Please enter a lowercase English letter")
            else:
                print("That letter doesn't appear in the word")
                used_letters.add(guess)
                attempts -= 1
    if guess_letters == word_set:
        print(word)
        print("You guessed the word")
        print("You survived")
    else:
        print("Thanks for playing!")
        print("We'll see how well you did in the next stage")


print("H A N G M A N")
menu = True
while menu:
    choose = input("Pick 1 to play or 0 to exit > ")
    if choose == "1":
        start_game()
    elif choose == "0":
        menu = False
