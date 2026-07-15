class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        self.head = None

    def get(self, index):
        current = self.head
        current_index = 0

        while current:
            if current_index == index:
                return current.val
            current = current.next
            current_index += 1

        return -1

    def addAtHead(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def addAtIndex(self, index, val):
        if index == 0:
            self.addAtHead(val)
            return

        current = self.head
        current_index = 0

        while current and current_index < index - 1:
            current = current.next
            current_index += 1

        if current is None:
            return

        new_node = Node(val)
        new_node.next = current.next
        current.next = new_node

    def deleteAtIndex(self, index):
        if self.head is None:
            return

        if index == 0:
            self.head = self.head.next
            return

        current = self.head
        current_index = 0

        while current.next and current_index < index - 1:
            current = current.next
            current_index += 1

        if current.next:
            current.next = current.next.next