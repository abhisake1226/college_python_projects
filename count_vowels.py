import sys

def count_vowels(line):
    vowels = 'aeiouAEIOU'
    count = sum(1 for char in line if char in vowels)
    return count

def copy_with_vowel_count(source_file, destination_file):
    try:
        with open(source_file, 'r') as source, open(destination_file, 'w') as destination:
            lines = source.readlines()
            if not lines:
                print("Source file is blank.")
                return
            for line in lines:
                vowel_count = count_vowels(line)
                destination.write(line.strip() + ' ' + str(vowel_count) + '\n')
        print("Content copied successfully with vowel count.")
    except FileNotFoundError:
        print("Source file not found.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python program.py source_file destination_file")
    else:
        source_file = sys.argv[1]
        destination_file = sys.argv[2]
        copy_with_vowel_count(source_file, destination_file)
