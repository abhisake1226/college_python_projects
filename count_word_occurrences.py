def count_word_occurrences(sentence, word):
    words = sentence.split()
    count = sum(1 for w in words if w == word)
    return count

def exchange_first_last_char(sentence):
    if len(sentence) <= 1:
        return sentence
    return sentence[-1] + sentence[1:-1] + sentence[0]

# Input multi-word string from the user
sentence = input("Enter a multi-word string: ")

# (a) Count the occurrences of a given word in the string
word = input("Enter a word to count its occurrences: ")
count = count_word_occurrences(sentence, word)
print("Count of the word is:", count)

# (b) Exchange the first and last characters of the string
modified_string = exchange_first_last_char(sentence)
print("Modified string:", modified_string)
