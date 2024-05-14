def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_len = self.get_length(head)
        """
        When n is equal to list_len, it means we need to remove the head node. However, in the loop, we are trying to access prev.next which is None when prev is the last node. This causes the AttributeError: 'NoneType' object has no attribute 'next' error.
To fix this, we need to add a special case to handle when n is equal to list_len. We can simply return head.next in this case, which will effectively remove the head node.
        """
        if n == list_len:
            return head.next

        prev = head
        for i in range(list_len - n - 1):
            prev = prev.next
        
        prev.next = prev.next.next
        return head
    
    def get_length(self, head: Optional[ListNode]) -> int:
        if head is None:
            return 0
        prev = head
        length = 0
        while prev:
            length += 1
            prev = prev.next
        return length