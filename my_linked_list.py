# The link list is a sequence of nodes having a similar data type, each node contains one data object and pointer to the next node.
class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next_node(self):
        return self.next_node

    def set_next(self, next):
        self.next_node = next
# functions of linked list
# init methods in a linked list


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            current = current.get_next()
            return count

    def search(self, nodeData):
        current = self.head
        isPresent = False
        while current and isPresent is False:
            if current.get_data() == nodeData:
                isPresent = True
            else:
                current = current.get_next()
                if current is None:
                    raise ValueError("No data found")
                return current
# delete the node


def delete(self, nodeData):
    current = self.head
    previous = None
    isPresent = True
    while current and isPresent is False:
        if current.get_data() == nodeData:
            isPresent = True
        else:
            previous = current
            current = current.get_next()
            if current is None:
                raise ValueError("No data found")
            if previous is None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())
