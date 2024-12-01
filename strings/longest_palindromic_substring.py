# Link: https://leetcode.com/problems/longest-palindromic-substring/description/

from collections import deque

class Solution:

    def check_if_palindrome(self, pstring: str) -> bool:
        size = len(pstring)
        if size == 0: return False
        start, end = 0, size - 1
        while start < end:
            if pstring[start] != pstring[end]: return False
            start += 1
            end -= 1
        return True

    # Dynamic programming approach is used
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        dp_set = set()
        if size == 0 or size == 1: return s
        que = deque()
        que.append(s)
        while len(que) != 0:
            s_item = que.popleft()
            s_size = len(s_item)
            if self.check_if_palindrome(s_item): return s_item
            if s_size > 2:
                sub_str1 = s_item[:s_size - 1]
                sub_str2 = s_item[1:]
                if sub_str1 not in dp_set:
                    que.append(sub_str1)
                    dp_set.add(sub_str1)
                if sub_str2 not in dp_set:
                    que.append(sub_str2)
                    dp_set.add(sub_str2)
        return s[0]

if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPalindrome("babaddtattarrattatddetartrateedredividerb"))
