
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = []
        c = head

        while c:
            arr.append(c)
            c = c.next

        idx = len(arr) - n

        if idx == 0:
            return head.next

        arr[idx - 1].next = arr[idx].next

        return head
