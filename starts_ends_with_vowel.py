def starts_ends_with_vowel(word):
    vowels = "aeiouAEIOU"
    return word[0] in vowels and word[-1] in vowels

def any_word_starts_ends_with_vowel(sentence):
    words = sentence.split()
    return any(starts_ends_with_vowel(word) for word in words)

# Example usage:
sample_data = [
    "Red Orange White",
    "Red White Black",
    "abcd dkise eosksu"
]

for data in sample_data:
    result = any_word_starts_ends_with_vowel(data)
    print(f'("{data}") -> {result}')
