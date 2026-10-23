class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None

        
class Linkedlist:
    def __init__(self):
        self.head = None
        self.len = 0
    def contains(self, val):
        current = self.head
        while current:
            if current.val == val:
                return True
            current = current.next
        return False

    def append(self, new):
        cur = self.head
        new_node = Node(new)
        if not cur:
            self.head = new_node
            self.len += 1
        else:
            while cur.next:
                cur = cur.next
            cur.next = new_node
            self.len += 1

    def remove(self, val):
        cur = self.head
        last = None
        while cur:
            if cur.val == val:
                if last is None:
                    self.head = cur.next
                else:
                    last.next = cur.next
                self.len -= 1
                return
            last = cur
            cur = cur.next
            