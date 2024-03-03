'''#question a

def find_numbers(N):
    count = 0
    numbers = []

    for num in range(1, N + 1):
        if num % 7 == 0 and num % 10 == 6:
            count += 1
            numbers.append(num)

    return numbers, count

def main():
    N = int(input("Enter the value of N: "))
    numbers, count = find_numbers(N)
    print("List of numbers:", numbers)
    print("Count of numbers:", count)

if __name__ == "__main__":
    main()
'''

#question b

def convert_case(names):
    converted_names = []
    for name in names:
        converted_name = ""
        for char in name:
            if char.isupper():
                converted_name += char.lower()
            elif char.islower():
                converted_name += char.upper()
            else:
                converted_name += char
        converted_names.append(converted_name)
    return converted_names

def main():
    num_names = int(input("Enter the number of names: "))
    names = []
    for _ in range(num_names):
        name = input("Enter a name: ")
        names.append(name)
    converted_names = convert_case(names)
    print("Converted names:", converted_names)

if __name__ == "__main__":
    main()
