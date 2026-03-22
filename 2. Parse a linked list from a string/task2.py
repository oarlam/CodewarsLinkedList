class Node:
    def __init__(self, data, next_n=None):
        self.data = data
        self.next = next_n

def linked_list_from_string(list_repr: str) -> Node | None:
    list_repr = list_repr.replace('-> None', '')
    list_repr = list_repr.replace('None', '')
    if not list_repr:
        return None
    list_repr = list_repr.split(' -> ')
    cur = Node(int(list_repr.pop(0)))
    start = cur
    for value in list_repr:
        next_n = Node(int(value))
        cur.next = next_n
        cur = next_n
    return start
