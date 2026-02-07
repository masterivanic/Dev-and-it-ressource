
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
            data =self.items.pop(0)
            self.rear -= 1
            return data
        

if __name__ == "__main__":
    q = ListQueue()
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    print(q.items, "before ----------")
    q.dequeue()
    print(q.items, "after  -------------")