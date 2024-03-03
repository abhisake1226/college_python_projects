class Queue:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size

    def add_element(self, element):
        if not self.list_full():
            self.queue.append(element)
            print(f"Added {element} to the queue.")
        else:
            print("Queue is full. Cannot add element.")

    def delete_element(self):
        if not self.list_empty():
            deleted_element = self.queue.pop(0)
            print(f"Deleted element: {deleted_element}")
            return deleted_element
        else:
            print("Queue is empty. Cannot delete element.")

    def list_full(self):
        return len(self.queue) >= self.max_size

    def list_empty(self):
        return len(self.queue) == 0


# Example usage:
queue = Queue(max_size=5)

queue.add_element(1)
queue.add_element(2)
queue.add_element(3)
queue.add_element(4)
queue.add_element(5)

queue.add_element(6)  # Should print "Queue is full. Cannot add element."

queue.delete_element()  # Should print "Deleted element: 1"
queue.delete_element()  # Should print "Deleted element: 2"
queue.delete_element()  # Should print "Deleted element: 3"
queue.delete_element()  # Should print "Deleted element: 4"
queue.delete_element()  # Should print "Deleted element: 5"

queue.delete_element()  # Should print "Queue is empty. Cannot delete element."
