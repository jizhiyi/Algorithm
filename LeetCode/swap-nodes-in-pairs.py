# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        xhead = ListNode(0)
        xhead.next = head
        q = xhead
        p = None
        while head is not None:
            if p is None:
                p = head
            else:
                q.next = head
                p.next = head.next
                head.next = p
                head = p
                p = None
                q = head
            head = head.next
        return xhead.next


def pr(head):
    p = head
    while p:
        print(p.val)
        p = p.next
    print('*'*45)


ls = ListNode(1)
ls.next = ListNode(2)
ls.next.next = ListNode(3)
ls.next.next.next = ListNode(4)
pr(ls)
pr(Solution().swapPairs(ls))
