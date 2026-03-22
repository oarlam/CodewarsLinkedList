class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def stringify(node):
    output = ''
    while node is not None:
        output += str(node.data) + ' -> '
        node = node.next
    return output + 'None'
