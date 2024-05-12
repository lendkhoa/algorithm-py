class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None
        self.prev = None


def insert(head: Node, new_data: int) -> Node:
    to_add = Node(new_data)
    prev = head
    while prev.next:
        prev = prev.next

    # prev---------|
    #  1 --> 2 --> 3 --> add_here
    prev.next = to_add
    return head


def insert_at(head: Node, new_data: int, position: int) -> Node:
    """
    Assume the position < len(head)
    """
    to_add = Node(new_data)
    if position == 0:
        to_add.next = head
        head = to_add
        return head
    prev = head
    for i in range(0, position - 1):
        prev = prev.next
    to_add.next = prev.next
    prev.next = to_add

    return head


def delete(head: Node, position: int) -> Node:
    """
    Assuming position < len(head)
    And position >= 0
    """
    if position == 0:
        head = head.next
        return head
    prev = head
    for i in range(0, position - 1):
        prev = prev.next
    prev.next = prev.next.next
    return head


def reverse(head: Node) -> Node:
    # 3 ptrs
    prev = None
    current = head
    while current:
        next = current.next
        print(
            f'> {current.data} | prev: {prev.data if prev else "Null"} | next {next.data if next else "Null"}'
        )
        current.next = prev
        prev = current
        current = next
    return prev


def add_two_numbers(l1: Node, l2: Node) -> Node:
    """
    Time: O(n)
    Space: O(1)
    """
    head = current = Node(-1)
    carry = 0
    while l1 or l2 or carry:
        if l1:
            # we only use 1 variable to keep track of the sum
            carry += l1.data
            l1 = l1.next
        if l2:
            carry += l2.data
            l2 = l2.next
        current.next = Node(carry % 10)
        carry //= 10
        current = current.next
    return head.next


def test_add_two_numbers():
    # create list 1
    a = Node(1)
    a.next = Node(2)
    a.next.next = Node(3)

    # create list 2
    b = Node(4)
    b.next = Node(9)

    result = add_two_numbers(a, b)
    print(f"Adding 123 + 49")
    print_linkedlist(result)


def test_insert_node_at_end_of_ll():
    # create a linked list
    root = Node(1)
    root.next = Node(2)
    root.next.next = Node(3)
    print_linkedlist(insert(root, 4))


def test_insert_node_at_specific_position():
    # create a linked list
    root = Node(1)
    root.next = Node(2)
    root.next.next = Node(3)
    print_linkedlist(insert_at(root, 4, 10))


def test_delete_node_at_specific_position():
    # create a linked list
    root = Node(1)
    root.next = Node(2)
    root.next.next = Node(3)
    print_linkedlist(delete(root, 1))


def test_reverse_doubly_ll():
    root = Node(1)
    root.next = Node(2)
    root.prev = None

    root.next.next = Node(3)
    root.next.prev = root

    root.next.next.prev = root.next
    print_linkedlist(reverse(root))


def print_linkedlist(head: Node):
    while head:
        print(f"{head.data}-", end=" ")
        head = head.next
    print("null")


# test_insert_node_at_end_of_ll()
# test_insert_node_at_specific_position()
# test_delete_node_at_specific_position()
test_reverse_doubly_ll()
# test_add_two_numbers()
