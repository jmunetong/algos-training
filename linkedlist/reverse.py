# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        Reverses a singly linked list.
        :param head: ListNode - the head of the linked list
        :return: ListNode - the new head of the reversed linked list
        """
        if head is None:
            return head

        prev = None
        current = head
        next_node = head.next

        while True:
            current.next = prev
            prev = current
            current = next_node
            if current is None:
                break
            next_node = current.next 
        
        return prev


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_list(prev, current, next_n):
            current.next = prev
            prev = current
            current = next_n
            if current is None:
                return prev
            next_n = current.next
            return reverse_list(prev, current, next_n)

        prev = None
        current = head
        if current is None:
            return head
        next_n = current.next
        start = reverse_list(prev, current, next_n)
        return start

       

        
        



# ----------------------------
# Helper functions for testing
# ----------------------------
def build_linked_list(values):
    """Builds a linked list from a Python list and returns the head."""
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def linked_list_to_list(head):
    """Converts a linked list back into a Python list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


if __name__ =='__main__':
        # Create a Solution instance
    sol = Solution()

    # Test 1: Empty list
    head = build_linked_list([])
    print(linked_list_to_list(sol.reverseList(head)))  # Expected: []

    # Test 2: Single node
    head = build_linked_list([1])
    print(linked_list_to_list(sol.reverseList(head)))  # Expected: [1]

    # Test 3: Two nodes
    head = build_linked_list([1, 2])
    print(linked_list_to_list(sol.reverseList(head)))  # Expected: [2, 1]

    # Test 4: Multiple nodes
    head = build_linked_list([1, 2, 3, 4, 5])
    print(linked_list_to_list(sol.reverseList(head)))  # Expected: [5, 4, 3, 2, 1]

    # Test 5: List with duplicates
    head = build_linked_list([1, 2, 2, 3])
    print(linked_list_to_list(sol.reverseList(head)))  # Expected: [3, 2, 2, 1]