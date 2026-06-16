import random

def play_hangman():
    # 1. Predefined list of 5 words
    word_list = ["python", "codealpha", "program", "developer", "internship"]
    chosen_word = random.choice(word_list)
    
    # Track guessed letters and remaining attempts
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = 6
    
    print("--- Welcome to CodeAlpha Hangman! ---")
    
    while incorrect_guesses < max_incorrect:
        # Display the current state of the word (e.g., p _ t h _ n)
        displayed_word = [letter if letter in guessed_letters else "_" for letter in chosen_word]
        print("\nWord to guess: " + " ".join(displayed_word))
        print(f"Attempts remaining: {max_incorrect - incorrect_guesses}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        
        # Get user input
        guess = input("Guess a letter: ").lower().strip()
        
        # Input Validation
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
            
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
            
        # Add to guessed letters
        guessed_letters.add(guess)
        
        # Check if the guess is right or wrong
        if guess in chosen_word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            incorrect_guesses += 1
            
        # Check for win condition
        if all(letter in guessed_letters for letter in chosen_word):
            print(f"\n🎉 Congratulations! You guessed the word: {chosen_word}")
            break
    else:
        print(f"\n❌ Game Over! You ran out of attempts. The word was: {chosen_word}")

if __name__ == "__main__":
    play_hangman()