class Stack:
    def __init__(self, max_size):
        self.stack = []
        self.max_size = max_size

    def push(self, item):
        if len(self.stack) >= self.max_size:
            print("Stack Overflow: Cannot push item, stack is full.")
            return
        self.stack.append(item)
        print(f"Pushed {item} into the stack.")

    def pop(self):
        if len(self.stack) == 0:
            print("Stack Underflow: Cannot pop item, stack is empty.")
            return None
        item = self.stack.pop()
        print(f"Popped {item} from the stack.")
        return item

    def peek(self):
        if len(self.stack) == 0:
            print("Peep operation failed: Stack is empty.")
            return None
        return self.stack[-1]


def main():
    max_size = int(input("Enter the maximum size of the stack: "))
    stack = Stack(max_size)

    while True:
        print("\nStack Operations:")
        print("1. Push")
        print("2. Pop")
        print("3. Peep")
        print("4. Quit")

        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            item = input("Enter item to push: ")
            stack.push(item)
        elif choice == 2:
            item = stack.pop()
            if item is not None:
                print("Popped item:", item)
        elif choice == 3:
            item = stack.peek()
            if item is not None:
                print("Top item in stack:", item)
        elif choice == 4:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
