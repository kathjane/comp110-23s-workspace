"""EX01 - Chardle: A cute step toward Wordle."""

__author__ = "730486658"

chardle_word: str = input("Enter a 5-character word: ")

chardle_word
if (len(chardle_word ) != 5):
    print("Error: Word must contain 5 characters")
    exit()

single_character: str = input("Enter a single character: ")
if(len(single_character) != 1):
    print("Error: Character must be a single character")
    exit()

count: int = 0

print("Searching for " + single_character  + " in " +  chardle_word)

if(single_character == chardle_word[0]):
    print(single_character + " found at index 0") 
    count = count + 1

if(single_character == chardle_word[1]):
    print(single_character + " found at index 1") 
    count = count + 1

if(single_character == chardle_word[2]):
    print(single_character + " found at index 2") 
    count = count + 1

if(single_character == chardle_word[3]):
    print(single_character + " found at index 3") 
    count = count + 1

if(single_character == chardle_word[4]):
    print(single_character + " found at index 4") 
    count = count +1

if(count == 0):
    print("No instances of " + single_character + " found in " + chardle_word)
if(count == 1):
        print("1 instance of " + single_character + " found in " + chardle_word)
if(count > 1):
         print(str(count) + " instances of " + single_character + " found in " + chardle_word)