1
11
21
1211


class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


def print_sequence(node: Node) -> int:
    num = 0
    print(f"\n This is a sequence")
    while node:
        print(f"{node.val}", end="")
        num = num * 10 + node.val
        node = node.next
    return num


def count_freq(number: int) -> Node:
    # 112 -> 2112
    digits = [int(digit) for digit in str(number)]

    if len(digits) == 1:
        count = Node(1)
        count.next = Node(digits[0])
        return count
    head = current = Node(-1)
    it = 0
    count = 0
    while it < len(digits):
        count += 1
        if it == 0:
            it += 1
            continue
        if digits[it] == digits[it - 1]:
            it += 1
        else:
            count = 0

        current.next = Node(count)
        current.next.next = Node(digits[it - 1])
        current = current.next.next

    return head.next


def convert_node_to_number(head: Node) -> int:
    num = 0
    while head:
        num = num * 10 + head.val
        print(f"\n current head {head.val} | num {num}")
        # print(f" \n !current num {num} | {head.val}")
        head = head.next
    print(f"  >>>> {num}")
    return num


def sequence(n: int, k: int):
    while k >= 0:
        print(f" Current n: {n}")
        node_sequence = count_freq(n)
        print_sequence(node_sequence)
        k -= 1
        # print(f" k: {k}")
        n = convert_node_to_number(node_sequence)


sequence(1, 3)
