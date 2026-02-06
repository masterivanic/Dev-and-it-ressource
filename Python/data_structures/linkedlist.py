
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def delete(self, data):
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                else:
                    prev.next = current.next
                self._size -= 1
                return
        prev = current
        current = current.next

    def delete_first_node(self):
        current = self.head
        if self.head is None:
            pass
        elif current == self.head:
            self.head = current.next

    def delete_last_node(self):
        current = self.head
        prev = self.head
        while current:
            if current.next is None:
                prev.next = current.next
                self._size -= 1
            prev = current
            current = current.next

    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def search(self, data):
        for node in self.iter():
            if data == node:
                return True
        return False

    def append_at_a_location(self, data, index):
        current = self.head
        prev = self.head
        node = Node(data)
        count = 1
        while current:
            if count == 1:
                node.next = current
                self.head = node
            elif count == index:
                node.next = current
                prev.next = node
            count += 1
            prev = current
            current = current.next
        if count < index:
            print("the list has less numbers of elements")

    def append1(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node

    def append(self, data): # worst method
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def clear(self):
        self.tail = None
        self.head = None
        self._size = 0


if __name__ == "__main__":
    
    words = SinglyLinkedList()
    words.append1("egg")
    words.append1("spam")
    words.append1("ham")

    words.delete_first_node()
    words.delete_last_node()
    words.delete("spam")
    print("------------------- + --------------------------------------")
    current = words.head
    while current:
        print(current.data)
        current = current.next

    print(words.search("egg"))
    print(words.search("ham"))
    print(words.size())