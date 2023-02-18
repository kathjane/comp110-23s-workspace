"""EX03: Wordle"""

__author__ = "730486658"

# defining the contain_char function
def contains_char(secret_word: str, letter_desired: str) -> bool:
    """Searches for a single character in a string"""
    assert len(letter_desired) == 1
    letter_idx: int = 0
    while letter_idx < len(secret_word):
        if letter_desired == secret_word[letter_idx]:
            return True
        else:
            letter_idx = letter_idx + 1
    return False

# defining the emojified function
def emojified(guess_word: str, secret_word: str) -> str:
    """Returns a string of emoji boxes colored based upon how close it is to the secret word"""
    #assert len(guess_word) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    letter_idx: int = 0

    result: str = ""

    while (letter_idx < len(secret_word)):
    # if the letter is in the right spot as the secret word print a green box
        if (secret_word[letter_idx] == guess_word[letter_idx]):
            result = result + GREEN_BOX
        else:
        # check if the letter is anywhere in the word
            if contains_char(secret_word, guess_word[letter_idx]) == True:
                result = result + YELLOW_BOX
            else: 
                result = result +WHITE_BOX
        letter_idx = letter_idx + 1    
    return result 

def input_guess(expected_length: int): 
    """Ensure that the input guess is the same length as the expected parameter"""
    guess_word: str = input("Enter a 5 character word: ")
    #guess_word
    while len(guess_word) != expected_length:
        guess_word = input("That wasn't " + str(expected_length) + " chars! Try again: ")
    return(guess_word)

def main() -> None: 
    """The entrypoint of the program and main game loop""" 
    secret_word: str = "codes"
    turn_idx: int = 1

    while turn_idx < 7:
        print(f"=== Turn {turn_idx}/6 === ")
        guess_word: str = (input_guess(5))
        print(emojified(guess_word, secret_word))
        if guess_word == secret_word:
            print(f"You won in {turn_idx}/6 turns! ")
            turn_idx = 7
        else:
            turn_idx = turn_idx + 1
    if guess_word != secret_word:
        print(f"X/6 - Sorry, try again tomorrow!")

               
if __name__ == "__main__":
    main()
    
