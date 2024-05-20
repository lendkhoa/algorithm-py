class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None
        self.prev = None


class NodeWithRandom:
    def __init__(
        self, data: int, random: "NodeWithRandom", next: "NodeWithRandom"
    ) -> None:
        self.data = data
        self.random = random
        self.next = next


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


def reverse_subparts(head: Node):
    """
    You are given a singly-linked list that contains N integers. A subpart of the list is a contiguous set of even elements, bordered either by either end of the list or an odd element. For example, if the list is [1, 2, 8, 9, 12, 16], the subparts of the list are [2, 8] and [12, 16].
    Then, for each subpart, the order of the elements is reversed. In the example, this would result in the new list, [1, 8, 2, 9, 16, 12].
    The goal of this question is: given a resulting list, determine the original order of the elements.
    Implementation detail:
    You must use the following definition for elements in the linked list:
    class Node {
        int data;
        Node next;
    }
    Signature
    Node reverse(Node head)
    Constraints
    1 <= N <= 1000, where N is the size of the list
    1 <= Li <= 10^9, where Li is the ith element of the list
    Example
    Input:
    N = 6
    list = [1, 2, 8, 9, 12, 16]
    Output:
    [1, 8, 2, 9, 16, 12]
    """

    def reverse_helper(head: Node, end: Node) -> Node:
        # 3 ptrs
        prev = None
        current = head
        print(f"  |_ head {head.data} -- end {end.data}")
        while current and current.data <= end.data:
            next = current.next
            current.next = prev
            prev = current
            current = next
            print(f"  |___ current {current.data if current else None}")
        print(f"  |_ after reverse")
        print_linkedlist(prev)
        return prev

    current = head
    prev = None
    start_index = None

    while current:
        next = current.next
        # print(f"Processing {current.data} | prev: {prev} | next: {next}")
        if (prev is None or prev.data % 2 != 0) and current.data % 2 == 0:
            print(f"  🏳️ Found start index {current.data}")
            start_index = current

        if next is None or next.data % 2 != 0 and current.data % 2 == 0:
            if start_index:
                # swap [start_index, current]
                save_next = current.next
                print(f"  🏁 Found end index {current.data}")
                current = reverse_helper(start_index, current)
                current.next = save_next
            else:
                prev = current
                current = next
        else:
            prev = current
            current = next

    return head


def deep_copy(head: NodeWithRandom) -> NodeWithRandom:
    """
    Returns the deep copy of the head.
    """
    # Step 1: create a new node next to the old node
    cur = head
    while cur:
        new_node = NodeWithRandom(cur.data, None, None)
        cur.next = new_node
        cur = new_node.next

    # Step 2: Update the random pointer
    cur = head
    while cur:
        if cur.random:
            cur.next.random = cur.random.next
        cur = cur.next.next  # go to the next node in the orginal list

    # Step 3: Unweave the pointer
    old_head = head
    new_head = head.next
    cur_old = old_head
    cur_new = new_head

    while cur_old:
        cur_old.next = cur_old.next.next
        cur_new.next = cur_new.next.next if cur_new.next else None
        cur_old = cur_old.next
        cur_new = cur_new.next

    return new_head


def test_deep_copy():
    # Create a new linked list
    first = NodeWithRandom(1, None, None)
    second = NodeWithRandom(2, None, None)
    third = NodeWithRandom(3, None, None)

    first.next = second
    second.next = third

    first.random = third
    third.random = second

    new_head = deep_copy(first)

    print(
        f"Comparing the old memory address {id(first)} | {first.data}  vs new {id(new_head)} | {new_head.data}"
    )
    print(f"Old: first.next vs second: {id(first.next)} vs {id(second)}")


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


def test_reverse_subparts():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(8)
    head.next.next.next = Node(9)
    head.next.next.next.next = Node(12)
    head.next.next.next.next.next = Node(16)
    print(f"------ Test 1-2-8-9-12-16 ------")
    print_linkedlist(reverse_subparts(head))


def print_linkedlist(head: Node):
    while head:
        print(f"{head.data}-", end=" ")
        head = head.next
    print("null")


# test_insert_node_at_end_of_ll()
# test_insert_node_at_specific_position()
# test_delete_node_at_specific_position()
# test_reverse_doubly_ll()
# test_add_two_numbers()
# test_reverse_subparts()
test_deep_copy()
