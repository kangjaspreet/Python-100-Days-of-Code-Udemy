import random
from hangman_words import word_list 
from hangman_art import logo, stages

# Print logo
print(f"{logo}\n\n\n")

chosen_word = random.choice(word_list)

display = ['_'] * len(chosen_word)
clean_display = ' '.join(display)
print(clean_display)

# Initialize
player_lives = 6
end_of_game = False
player_guesses = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in player_guesses:
        print(f"You've already guessed {guess}! Please guess another letter.")
    elif guess not in chosen_word:
        player_guesses.append(guess)
        player_lives -= 1
        print(f"{guess} is not in the word. You have {player_lives} guesses remaining.\n{stages[player_lives]}")
    else:
        player_guesses.append(guess)
        for i in range(0, len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
                clean_display = ' '.join(display)
    
    print(clean_display)

    # Check if the player lost
    if player_lives == 0:
        end_of_game = True
        print(f"Game over! You lose :(\nThe word was {chosen_word}.")
    
    # Check if the player won
    if ('_' not in display):
        end_of_game = True
        print("You win!")