import random

def hangman():
    # List of words for the game
    words = ['apple', 'banana', 'orange', 'grape', 'pineapple', 'strawberry', 'watermelon']
    chosen_word = random.choice(words)  # Randomly select a word
    word_length = len(chosen_word)
    tries_left = 6  # Number of incorrect tries allowed
    guessed_letters = []  # List to store guessed letters
    guessed_word = ['_'] * word_length  # List to track guessed parts of the word
    game_over = False
    
    print("Welcome to Hangman!")
    print("Try to guess the word.")

    while not game_over:
        # Display current state of the word
        print("Word to guess:", ' '.join(guessed_word))
        
        # Prompt for user input
        guess = input("Guess a letter or the full word: ").lower()

        # Handle single letter guess
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already guessed that letter. Try again.")
            elif guess in chosen_word:
                print("Good guess!")
                # Update guessed_word with correct guess
                for i in range(word_length):
                    if chosen_word[i] == guess:
                        guessed_word[i] = guess
                guessed_letters.append(guess)
            else:
                print("Oops! That letter is not in the word.")
                tries_left -= 1
                guessed_letters.append(guess)
        
        # Handle full word guess
        elif len(guess) == word_length and guess.isalpha():
            if guess == chosen_word:
                guessed_word = list(chosen_word)  # Reveal the entire word
            else:
                print("Incorrect guess!")
                tries_left -= 1
        
        # Handle invalid input
        else:
            print("Invalid input. Please enter a single letter or the full word.")

        # Display tries left and guessed letters
        print(f"Tries left: {tries_left}")
        print("Guessed letters:", ' '.join(guessed_letters))

        # Check if the player has won or lost
        if '_' not in guessed_word:
            print("Congratulations! You guessed the word correctly.")
            game_over = True
        elif tries_left == 0:
            print("Sorry, you ran out of tries. The word was:", chosen_word)
            game_over = True

    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        hangman()  # Restart the game
    else:
        print("Thanks for playing Hangman!")

# Start the game
hangman()
