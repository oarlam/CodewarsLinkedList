class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    cur = Node(data)
    cur.next = head
    return cur

def build_one_two_three():
    cur = None
    for val in range(3, 0, -1):
        cur = push(cur, val)
    return cur
