class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, element):
        self.items.append(element)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty.")
            return None

    def is_empty(self):
        return len(self.items) == 0


# Example usage:
queue = Queue()

# Enqueue elements
queue.enqueue(5)
queue.enqueue(10)
queue.enqueue(15)

# Check if queue is empty
print("Is the queue empty?", queue.is_empty())

# Dequeue elements
print("Dequeued element:", queue.dequeue())
print("Dequeued element:", queue.dequeue())
print("Dequeued element:", queue.dequeue())

# Check if queue is empty after dequeuing all elements
print("Is the queue empty?", queue.is_empty())
