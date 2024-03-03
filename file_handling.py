def process_file(filename):
    try:
        # Open the file for reading
        with open(filename, 'r') as file:
            # Read the content of the file
            content = file.read()
        
        # Read a character from user input
        char = input("Enter a character to remove from the file content: ")

        # Check if the character is found in the file content
        if char not in content:
            print("The character is not found in the file.")
            return

        # Remove every occurrence of the inputted character from the content
        content_without_char = content.replace(char, '')

        # Display the modified content
        print("File content after removing occurrences of the character:")
        print(content_without_char)

    except FileNotFoundError:
        print("File not found.")

# Example usage:
filename = "source.txt"
process_file(filename)

"""Write a Python function that reads a text file and do the following operations :
(a) Read any character from user input that is supposed to be found at least once in that input file.
(b) If inputted character is not found in file, then report the issue and ask to re-enter other character.
(c) Remove every occurrences of the inputted character, store and display the rest of file content."""
