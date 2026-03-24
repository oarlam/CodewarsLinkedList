class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def swap_pairs(head):
    if head is None or head.next is None:
        return head
    dummy = Node(None)
    dummy.next = head
    prev = dummy
    while prev.next and prev.next.next:
        node1 = prev.next
        node2 = prev.next.next
        node1.next, node2.next = node2.next, node1
        prev.next = node2
        prev = node1
    return dummy.next
