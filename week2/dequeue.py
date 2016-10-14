class LinkedDequeue:

    class Node:

        def __init__(self, item, next=None):
            self.item = item
            self.next = next

    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first == None

    def enqueue(self, item):
        old_last = self.last
        self.last = self.Node(item)
        if self.is_empty():
            self.first = self.last
        else:
            old_last.next = self.last
    
    def dequeue(self):
        item = self.first.item
        self.first = self.first.next
        if self.is_empty():
            self.last = None
        return item

# TODO array version?
