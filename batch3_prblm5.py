"""Given a string S of lower case characters. The task is to check whether the given string is Heterogram 
or not. A heterogram is a word, phrase, or sentence in which no letter of the alphabet occurs more than 
once. Examples : 
Input : S= "the big dwarf only jumps" 
Output : Yes 
Each letter in the string S has occurred only once. Write a program in Python to perform the said task."""

def is_heterogram(string):
    # Convert the string to lowercase to handle case-insensitive comparison
    string = string.lower()
    # Remove spaces from the string
    string = string.replace(" ", "")
    # Create a set of characters from the string
    char_set = set(string)
    # Compare the length of the original string with the length of the character set
    return len(string) == len(char_set)

# Test the function with the given example
string = "the big dwarf only jumps"
if is_heterogram(string):
    print("Yes")
else:
    print("No")
