class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        sum_list = ListNode(0)
        p = sum_list
        s = 0
        while l1 or l2 or s:
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next
            p.next = ListNode(s % 10)
            p = p.next
            s /= 10
        return sum_list.next

solution = Solution()
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
l = solution.addTwoNumbers(l1, l2)
while l:
    print l.val
    l = l.next
