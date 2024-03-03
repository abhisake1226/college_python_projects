S1 = "I Love ICE CREAM"

# (a) Print all the words having occurrences of 'e'
print("(a) Words with occurrences of 'e':")
words_with_e = [word for word in S1.split() if 'e' in word.lower()]
print(words_with_e)

# (b) Output will be "I love ice cream"
print("\n(b) Output with lowercase:")
lowercase_output = S1.lower()
print(lowercase_output)

# (c) Reverse the string
print("\n(c) Reversed string:")
reversed_string = S1[::-1]
print(reversed_string)

# (d) Check if S1 starts with 'I'
print("\n(d) Does S1 start with 'I'?")
starts_with_I = S1.startswith('I')
print(starts_with_I)

# (e) Replace 'ICE CREAM' in S1 with 'HOCKEY'
print("\n(e) String after replacing 'ICE CREAM' with 'HOCKEY':")
replaced_string = S1.replace('ICE CREAM', 'HOCKEY')
print(replaced_string)
