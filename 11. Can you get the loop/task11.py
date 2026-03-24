class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def loop_size(node):
    slow = node
    fast = node.next

    while slow != fast:
        slow = slow.next
        fast = fast.next.next

    start = fast
    fast = fast.next
    n = 1
    while fast != start:
        fast = fast.next
        n += 1
    return n
