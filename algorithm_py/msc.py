def mergeTwoLists(
    self, list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    head = ListNode(-1)
    prev = head

    while list1 and list2:
        if list1.val <= list2.val:
            prev.next = list1
            list1 = list1.next
        else:
            prev.next = list2
            list2 = list2.next
        prev = prev.next

    # at least one of l1 and l2 can still have nodes at this point
    prev.next = list1 or list2
    return head.next
