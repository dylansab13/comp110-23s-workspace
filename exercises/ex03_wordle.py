"""EX03 - Wordle - Improving The Game."""

__author__ = "730488390"

word_indx: int = 0
the_emoj: str = ""



# If the character is found within the first string, return True, if not, False
def contains_char(word_check: str, chr_srch: str) -> bool:
    """Returns True if chr is found at indx of first string"""
    assert len(chr_srch) == 1
    word_indx: int = 0
    while word_indx < len(word_check):
        if word_check[word_indx] == chr_srch:
            return True
        word_indx = word_indx + 1
    return False
   

def emojified(word_guess: str, the_secret: str) -> str:
    """Function returns string of emoji of different colors"""
    assert len(word_guess) == len(the_secret)
    # Box colors depending on if the letter is in the right spot
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    the_emoj = ""
    word_indx = 0 
# Loop through the guessed word, if letter is is right spot, add green box
    while word_indx < len(word_guess):

        if word_guess[word_indx] == the_secret[word_indx]:
            the_emoj += GREEN_BOX
        else:
            within_wrd = contains_char(the_secret, word_guess[word_indx])
            if within_wrd:
                the_emoj += YELLOW_BOX
            else: 
                the_emoj += WHITE_BOX
        word_indx += 1

    return the_emoj

# Check to see if guess is the same length as expected, if not, tell user it wasn't thr right length 
def input_guess(expected_length: int) -> str:
    """Function for 5 character word"""
    while True:
        guess = input(f"Enter a {expected_length} character word: ")
        if len(guess) == expected_length:
            return guess
        else:
            print(f"That wasn't {expected_length} chars! Try again: ")


# Function for the main game, includes attempt number, max attempts, and the word to win
def main() -> None:
    """The entrypoint of the program and main game loop."""
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

if __name__ == "__main__":
    main()
