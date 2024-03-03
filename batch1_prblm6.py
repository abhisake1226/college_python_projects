class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        '''Add an item to the top of the stack'''
        self.items.append(item)

    def pop(self):
        '''Remove and return the top item from the stack '''
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        '''Return the top item from stack without removing it'''
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        '''Check if the stack is empty'''
        return len(self.items) == 0

if __name__=="__main__":
    stack = Stack()

    #pushing elements onto the stack
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(34)

    #check if the stack is empty
    print("Is stack is empty :",stack.is_empty())

    #peeking at the top of the stack
    print("Top element of the stack: ",stack.peek())

    #Popping elements from the stack
    print("Popped element: ",stack.pop())
    print("Popped element: ",stack.pop())
    print("Popped element: ",stack.pop())
    print("Popped element: ",stack.pop())

    #check if the stack is empty
    print("Is stack is empty :",stack.is_empty())
