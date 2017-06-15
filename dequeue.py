class LinkedDequeue:

    class _Node:

        def __init__(self, _item, _next=None):
            self._item = _item
            self._next = _next

    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first == None

    def enqueue(self, item):
        old_last = self.last
        self.last = self._Node(item)
        if self.is_empty():
            self.first = self.last
        else:
            old_last._next = self.last
    
    def dequeue(self):
        item = self.first._item
        self.first = self.first._next
        if self.is_empty():
            self.last = None
        return item

# TODO array version?
