class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        n = Node(value)
        n.next = self.head
        self.head = n

    def includes(self, value):
        temp = self.head # don't want to mess with actual self.head
        while temp is not None:
            if temp.value == value:
                return True
            temp = temp.next
        return False

    def __str__(self):
        output_str = ""
        temp = self.head
        while temp is not None:
            output_str = output_str + "{ " + temp.value + " } -> "
            temp = temp.next
        return output_str + "NULL"


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None