
class ListQueue:
    def __init__(self):
        self.items = []
        self.front = self.rear = 0
        self.size = 3

    def enqueue(self,data):
        if self.size == self.rear:
            print("Queue is full")
        else:
            self.items.append(data)
            self.rear += 1

    def dequeue(self):
        if self.rear == self.front:
            print("Queue is empty")
        else:
            data = self.items.pop(0)
            self.rear -= 1
            return data
        

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class Queue:
    """
    Queue base on double linkedlist
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    def enqueue(self, data):
        node = Node(data, None, None)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.count += 1

    def dequeue(self):
        if self.count == 1:
            self.head = None
            self.tail = None
            self.count -= 1
        elif self.count > 1:
            self.head = self.head.next
            self.head.prev = None
        elif self.count < 1:
            print("Queue is empty")
        self.count -= 1


if __name__ == "__main__":
    q = ListQueue()
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    print(q.items, "before ----------")
    q.dequeue()
    print(q.items, "after  -------------")