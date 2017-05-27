class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return None
        n = len(lists)
        if n == 1:
            return lists[0]
        p1 = Solution.mergeKLists(self, lists[:n / 2])
        p2 = Solution.mergeKLists(self, lists[n / 2:])
        dummy = ListNode(0)
        p = dummy
        while p1 or p2:
            if not p2 or (p1 and p1.val < p2.val):
                p.next = ListNode(p1.val)
                p1 = p1.next
            else:
                p.next = ListNode(p2.val)
                p2 = p2.next
            p = p.next
        return dummy.next

p1 = ListNode(3)
p1.next = ListNode(4)
p1.next.next = ListNode(5)
p2 = ListNode(1)
p2.next = ListNode(5)
solution = Solution()
p = solution.mergeKLists([p1, p2])
while p:
    print p.val
    p = p.next
