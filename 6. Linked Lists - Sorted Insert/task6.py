""" For your information:"""
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    new_node = Node(data)
    idk = Node(None)
    idk.next = head
    cur = idk
    while True:
        if cur.next is None:
            cur.next = new_node
            break
        if cur.next.data > data:
            new_node.next = cur.next
            cur.next = new_node
            break
        cur = cur.next
    return idk.next
    # Your code goes here.
    # Make sure to return the head of the list.
