class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if not head.next:
        raise ValueError('splitting a single node')
    head2 = head.next
    node1 = head
    node2 = node1.next
    while node1 and node2:
        node1.next = node2.next
        try:
            node2.next = node2.next.next
        except AttributeError:
            node2.next = None
        node1 = node1.next
        node2 = node2.next
    return Context(head, head2)
