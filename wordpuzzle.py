# Project Description
# The program contains a hidden secret word stored in a variable. This word can have any number of letters
# in it. When the program runs, the user is shown underscores ( _ ) for each letter of the word.

# The user then enters a guess. If the guess is correct, the user wins and the game is over.

# If the guess is not correct, the user will be given a hint to help them improve their guess for 
# the next round.

# The game continues prompting the user for new guesses and showing them hints until they guess the 

# word correctly. When the game is over, the program displays the number of guesses that were made.

# The guess must be the same number of letters as the secret word. If the guess has a different numbers
# of letters, the user is given a message explaining this, and no hint is provided.

# The hint shows the letters of the guess, but each letter is rendered in a special way as follows:

# An underscore _ indicates that the letter was not present in the secret word.

# A lowercase letter indicates that the letter was present somewhere in the secret word, but not at that
# position.

# An uppercase letter indicates that the letter was present at that exact spot in the secret word. 
# (In other words, if the second letter in the guess is also the second letter in the secret word, 
# then that letter is shown as a capital.)
# Because capital letters have meaning in our hints, the secret word should be all lower case. Similarly, 
# when the user enters their guess, you should convert it to lowercase prior to checking for matches.
# Final Requirements
# In addition to the Milestone requirements, your final program must:

# Use a loop to generate the initial hint.

# Add a check to verify that the length of the guess is the same as the length of the secret word.
# If it is not, display a message. If they are the same, then proceed to give the hint.

# Add the hints according to the rules above.

# Make sure to account for the following in your hints:

# Letters that are not present at all in the secret word (underscore _).

# Letters that are present in the secret word, but in a different spot (lowercase).

# Letters that are present in the secret word at that exact spot spot (uppercase).

# Additionally, be sure to add a space after every character in the hint as in the examples above.

# Showing Creativity and Exceeding Requirements
# Once you have the basic rules of the game in place, consider adding something extra to the hints, 
# other rules or limitations to the number of guesses, or anything else you think would be fun.
# Important: In order to receive credit for showing creativity, you must include a comment
#  at the top of the program that describes in 1-2 sentences what you have added.

#coding starts here...

# Secret word to be guessed
secret_word = "stanley"
guess_count = 0  # Number of guesses made

while True:
    # Display the initial hint (all underscores for each letter of the word)
    hint = "_ " * len(secret_word)
    print("Your hint is:", hint.strip())  

    # Get the user's guess
    guess = input("What is your guess? ").lower()
    guess_count += 1  # Increment guess count

    # Check if the guess has the same length as the secret word
    if len(guess) != len(secret_word):
        print("Sorry, the guess must have the same number of letters as the secret word.")
        continue  # If not, ask the user to guess again

    # If the guess is correct, end the game
    if guess == secret_word:
        print(f"Congratulations! You guessed it!")
        print(f"It took you {guess_count} guesses.")
        break  # Exit the loop and end the game

    # Generate the hint based on the guess
    hint_list = [] * len(secret_word)  # Initialize hint list with placeholders
    # Initialize hint list with underscores
    hint_list = ["_"] * len(secret_word)  # Placeholder for incorrect letters
    # Check for correct letters in the correct position (uppercase letters)
    # and incorrect position (lowercase letters)

    # Check for exact matches (uppercase letters)
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            hint_list.append(guess[i].upper())  # Capitalize the letter if it matches
        else:
            hint_list.append(None)  # Placeholder for non-matches

    # Check for incorrect position but correct letter (lowercase letters)
    for i in range(len(secret_word)):
        if hint_list[i] is None:  # Only check non-matches
            if guess[i] in secret_word:
                hint_list[i] = guess[i].lower()  # Lowercase for wrong position
            else:
                hint_list[i] = "_"  # Underscore for incorrect letters

    # Display the hint
    print("Your hint is:", " ".join(hint_list))
