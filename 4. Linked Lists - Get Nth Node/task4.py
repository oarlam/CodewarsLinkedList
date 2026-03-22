class Node(object):
    """Node class for reference"""
    def __init__(self, data, next_n=None):
        self.data = data
        self.next = next_n

def get_nth(node, index):
    if not node or index < 0:
        raise ValueError
    for _ in range(index):
        if node.next is None:
            raise IndexError
        node = node.next
    return node
