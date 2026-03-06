print("Welcome to Hangman")

# We need the computer to pick a RANDOM word
import random

# We need the computer to choose from a LIST of words
words = ["mascara", "powder", "necklace", "bracelets", "lipstick", "eyeliner", "perfume", "foundation"]

# Store the randomly selected word in a variable reference
secret_word = random.choice(words)

# print(secret_word)

# Part 2
# We need to display the secret word without the letters for people to guess


# We need to create a way for people to guess letters
guess = input("Guess a letter: ").strip().lower()


# We need to create a way to check if letter player used is in secret word

display = []
guessed_letter = [] 
# For each letter in our secret word, we want to append _ to our display
for letter in secret_word:
    display.append("_")

# print(secret_word)
# print(display)

# We need to create a way if letter player used is in the secret word
# for each position in our secret word, if the letter the player picks is in that secret word, then find that position in our display and replace it
for position in range(len(secret_word)):
    secret_word_letter = secret_word[position]

    if secret_word_letter == guess:
        display[position] = guess

print(display)

# while the word is not complete, and the game is not over, we get prompted for new guess
game_over = False
lives = 4
while not game_over:
    guess = input("Guess a letter: ").strip().lower()

    if(len(guess)) != 1:
        print("Please enter a single letter")
        continue 
    if guess in guessed_letter:
        print("You already guessed that letter, try again")
        continue 
    guessed_letter.append(guess) 
    print("Guessed letters: ", guessed_letter)
    if guess not in secret_word:
        lives -= 1 
        print('Wrong guess, try again. Lives left: ', lives)
        if lives == 0:
            game_over = True
            print("You lose! The secret word was: ", secret_word)
            break
# We need to create a way to check if the player is in secret word

    for position in range(len(secret_word)):
        secret_word_letter = secret_word[position]

        if secret_word_letter == guess:
            display[position] = guess

    print(display)

    # Check if the game is complete
    if "_" not in display:
        game_over = True
        print("You are a smart cookie = You win!") 

# print(len("Mississippi"))
# print(len(""))