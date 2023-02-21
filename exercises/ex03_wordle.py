"""EX03 - Wordle - Improving The Game."""

__author__ = "730488390"

word_indx: int = 0
the_emoj: str = ""

# Box colors depending on if the letter is in the right spot
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# If the character is found within the first string, return True, if not, False
def contains_char(word_check: str, chr_srch: str) -> bool:
    """Returns True if chr is found at indx of first string"""
    # Makes sure the length of the second parameter is one character
    assert len(chr_srch) == 1
    word_indx: int = 0
    while word_indx < len(word_check):
        if word_check[word_indx] == chr_srch:
            return True
        word_indx = word_indx + 1
    return False
   

def emojified(word_guess: str, the_secret: str) -> str:
    """Function returns string of emoji of different colors"""
# Check to make sure the two parameters are the same length
    assert len(word_guess) == len(the_secret)

    the_emoj = ""
    word_indx = 0 
# Loop through the guessed word, if letter is is right spot, add green box
    while word_indx < len(word_guess):

        if word_guess[word_indx] == the_secret[word_indx]:
            the_emoj += GREEN_BOX
        else:
            within_wrd = False
            dif_indx = 0
            found = False
# Loop through secret word to see if the character is in there but in wrong spot, if so, yellow box
            while dif_indx < len(the_secret) and not found:
                if the_secret[dif_indx] == word_guess[word_indx]:
                    within_wrd = True
                    found = True
                dif_indx += 1
            if within_wrd:
                the_emoj += YELLOW_BOX
            else:
                # Add white box if character is not in the secret word
                the_emoj += WHITE_BOX
        word_indx += 1

    return the_emoj

# Check to see if guess is the same length as expected, if not, tell user it wasn't thr right length 
def input_guess(expected_length: int) -> str:
    """Function for 5 character word"""
    while True:
        guess: str = input(f"Enter a {expected_length} character word:")
        if len(guess) == expected_length:
            return guess
        else:
            guess = input(f"That wasn't {expected_length} chars! Try again: ")


# Function for the main game
def main() -> None:
    """The entrypoint of the program and main game loop."""
    # The word to win the game, attempt number, max attempts for the game
    the_secret = "codes"
    attempt_num = 1
    max_attempt = 6

# The loop which keeps track of guesses in the game, if the user wins, or if the user loses
    while attempt_num <= max_attempt:
        print(f"=== Turn {attempt_num}/{max_attempt} ===")
        word_guess = input_guess(len(the_secret))
        the_emoj = emojified(word_guess, the_secret)
        print(the_emoj)

        if word_guess == the_secret:
            print(f"You won in {attempt_num}/{max_attempt} turns!")
            return
        attempt_num += 1

    print(f"X/{max_attempt} - Sorry, try again tomorrow! ")

# Function Call
main()

if __name__ == "__main__":
    main()
