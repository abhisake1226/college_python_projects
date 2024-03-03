def hash_display(filename):
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Read the content of the file
            content = file.read()

            # Initialize an empty string to store the formatted content
            formatted_content = ""

            # Iterate over each character in the content
            for char in content:
                # If the character is a space, replace it with "$"
                if char == ' ':
                    formatted_content += '$'
                # Otherwise, append the character followed by "#"
                else:
                    formatted_content += char + '#'

            # Print the formatted content
            print(formatted_content)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

# Test the function with the given example file
hash_display("matter.txt")
