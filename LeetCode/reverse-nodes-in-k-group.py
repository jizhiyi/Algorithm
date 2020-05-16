# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverse(self, head, tail, k):
        p = head
        for i in range(k-1):
            tmp = p.next
            p.next = p.next.next
            tmp.next = head
            head = tmp
        return head, p

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        xhead = ListNode(0)
        xhead.next = head
        pre = xhead
        while head is not None:
            tail = pre
            for i in range(k):
                tail = tail.next
                if tail is None:
                    return xhead.next
            # 保存后面的
            n = tail.next
            # 交换
            # print(head.val, tail.val)
            # input()
            head, tail = self.reverse(head, tail, k)
            # print(head.val, tail.val)
            # input()
            pre.next = head
            tail.next = n
            pre = tail
            head = tail.next
            # pr(xhead)
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
ls.next.next.next.next = ListNode(5)
pr(Solution().reverseKGroup(ls, 3))
