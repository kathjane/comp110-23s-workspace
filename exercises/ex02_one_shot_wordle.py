"""EX02: One shot wordle."""

__author__ = "730486658"

# define variables
secret_word: str = "python"
word_guess: str = input(f"What is your {len(secret_word)}-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
letter_idx: int = 0

result: str = "" 

# make sure word is the right amount of letters
while (len(word_guess) != len(secret_word)):
    word_guess = input(f"That was not {len(secret_word)} Letters! Try again: ")

# while loop to check all letters
while (letter_idx < len(secret_word)):
    letter_anywhere: bool = False
    compare_idx: int = 0
    # if the letter is in the right spot as the secret word print a green box
    if (secret_word[letter_idx] == word_guess[letter_idx]):
        result = result + GREEN_BOX
    else:
        # check if the letter is anywhere in the word
        while (not letter_anywhere and compare_idx < len(secret_word)):
            if (secret_word[compare_idx] == word_guess[letter_idx]):
                letter_anywhere = True
            else:
                compare_idx = compare_idx + 1 
        if letter_anywhere is True:
            result = result + YELLOW_BOX
        else:
            result = result + WHITE_BOX  
    letter_idx = letter_idx + 1    

print(result)  

# check to see if the secret word is right
if (word_guess == secret_word):
    print("Woo! You got it! ")
else:
    print("Not quite. Play again soon! ")
