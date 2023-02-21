

def mimic(my_words: str) -> str:
    """Given the string my_words, outputs the same string"""
    return my_words


print(mimic("Hello!"))

my_words: str = ("Hello")
response: str = mimic(my_words)

print(response)

def mimic(my_word: str, my_index: int) -> str:
    """Input string and index, returns letter of index"""
    if my_index >= len(my_word):
        return("Too high of an endex")
    return(my_word[my_index])

print(mimic("hello", 4))
   