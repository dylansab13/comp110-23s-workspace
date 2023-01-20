"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730488390"

five_C = str(input("Enter a 5-character word:"))
if len(five_C) != 5:
    print("Error: Word must contain 5 characters")
    exit()

single_C = str(input("Enter a single character:"))
if len(single_C) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + single_C + " in " + five_C)
matching_C = 0

if single_C == five_C[0]:
    print(single_C + " found at index 0")
    matching_C += 1
    
if single_C == five_C[1]:
    print(single_C + " found at index 1")
    matching_C += 1

if single_C == five_C[2]:
    print(single_C + " found at index 2")
    matching_C += 1
    
if single_C == five_C[3]:
    print(single_C + " found at index 3")
    matching_C += 1
    
if single_C == five_C[4]:
    print(single_C + " found at index 4")
    matching_C += 1
    
if matching_C == 0:
    print("No instances of " + single_C + " found in" + five_C)

if matching_C == 1:
    print(str(matching_C) + " instance of " + single_C + " found in " + five_C)

else: 
    print(str(matching_C) + " instances of " + single_C + " found in" + five_C)