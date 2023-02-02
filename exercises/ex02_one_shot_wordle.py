"""EX02 - Wordle - Creating The Game"""

__author__ = "730488390"


# Defining all of my variables
secret_word: str = "python"
word_indx: int = 0
the_emoj: str = ""
six_C: str = input(f"What is your {len(secret_word)} guess?")

# Defining the box colors for different meanings
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# Seeing if their chosen word is six letters 
while len(six_C) != len(secret_word):
    six_C = (input(f"That was not {len(secret_word)} letters! Try again:"))

# If it is 6 letters, great, if not, not so great
if six_C == secret_word:
    print("Woo! You got it!")
else: 
    print("Not quite. Play again soon!")
   
# Loop to see if index is in the word 
while word_indx < len(secret_word):
    
# If the index of the guessed word is the same index of the real word, a green box appears
    if six_C[word_indx] == secret_word[word_indx]:
        the_emoj += GREEN_BOX
# If it is not the same, set a variable for a letter in the secret word at a different index
    else:
        letter_in: bool = False
        dif_indx: int = 0
# If a letter in guessed word is in the actual word and new index is in the six letter word     
        while letter_in is False and dif_indx < len(secret_word):
            if secret_word[dif_indx] == six_C[word_indx]:
                letter_in = True
            dif_indx = dif_indx + 1
# If there is a letter in guessed word that is in the actual word but at a different index, yellow square shows, if it is not in the actual word, white box appears
        if letter_in is True:
            the_emoj = the_emoj + YELLOW_BOX
        else:
            the_emoj += WHITE_BOX
    word_indx += 1
# Print what is correct and incorrect 
print(the_emoj)

