import random
import 03_(b)_Hangman_Art_and_Words
import os

stage = hangman_art_and_words.stages
w_list = hangman_art_and_words.word_list

chosen_word = random.choice(w_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
print("Welcome to Stefan's: HANGMAN Game!\n")
print(f"You get a word with {word_length} letters.")

display = []
user_list = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    os.system('cls' if os.name == 'nt' else 'clear')

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    if guess in user_list:
        lives += 1

    if guess not in user_list:
        user_list += guess
    else:
        print(f"You already entered {guess}")

    if guess not in chosen_word:
        lives -= 1
        print("Your letter is not in word.")
        if lives == 0:
            end_of_game = True
            print(f"{'-' * 20}\n    You lose!  \n{'-' * 20}\nYour word was: {chosen_word}")

    print(stage[lives])
    print(f"You have left: {lives} lives.\n")
    print(f"{' '.join(display)}\n")

    if "_" not in display:
        end_of_game = True
        print(" * * * You win! * * * ")
