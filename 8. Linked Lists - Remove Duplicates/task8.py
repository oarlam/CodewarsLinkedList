class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    cur = head
    while True:
        if cur is None or cur.next is None:
            return head
        if cur.data == cur.next.data:
            cur.next = cur.next.next
        else:
            cur = cur.next
