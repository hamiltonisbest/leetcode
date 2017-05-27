class Solution(object):
    def isValid(self, s):
        if not s or len(s) % 2 != 0:
            return False
        q = []
        matches = {')':'(', ']':'[', '}':'{'}
        for c in s:
            if c == '(' or c == '[' or c == '{':
                q.append(c)
            else:
                if len(q) == 0 or q[-1] != matches[c]:
                    return False
                else:
                    del q[-1]
        return len(q) == 0

print Solution().isValid('[]{()}')
