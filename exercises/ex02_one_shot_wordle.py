"""EX02: One shot wordle"""

__author__ = "730486658"

# define variables
secret_word: str = "python"
word_guess: str = input(f"What is your {len(secret_word)}-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
letter_idx: int = 0
letter_anywhere: bool = False
all_letters: int = 0
result: str = "" 

# make sure your word is 6 letters
while (len(word_guess) != len(secret_word)):
    word_guess: str = input(f"That was not {len(secret_word)} Letters! Try again: ")

while (letter_idx < len(secret_word)):
    if(secret_word[letter_idx] == word_guess[letter_idx]):
        result = result + GREEN_BOX
        while (letter_anywhere and letter_idx < len(secret_word)):
            if (all_letters == word_guess[letter_idx]):
                letter_anywhere = True
                result = result + YELLOW_BOX    
            else:
                letter_idx = letter_idx + 1 
    else:
        result = result + WHITE_BOX
    letter_idx = letter_idx + 1    

print(result)  

# check to see if the secret word is right
if (word_guess == secret_word):
     print("Woo! You got it! ")
else:
    print("Not quite. Play again soon! ")

