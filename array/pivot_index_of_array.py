# Link: https://www.geeksforgeeks.org/equilibrium-index-of-an-array/
# Link: https://leetcode.com/problems/find-pivot-index/description/
from typing import List

class Solution:

    def prefix_sum(self, nums):
        size = len(nums)
        prefix_sum = [-1] * size
        p_sum = 0
        for i in range(size):
            p_sum += nums[i]
            prefix_sum[i] = p_sum
        return prefix_sum

    def pivot_index(self, nums: List[int]) -> int:
        prefix_sum = self.prefix_sum(nums)
        suffix_sum = self.prefix_sum(nums[::-1])[::-1]
        for i in range(len(nums)):
            if prefix_sum[i] == suffix_sum[i]:
                return i
        return -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.pivot_index([1, 3, -1, 1, -1, 5, 6, -7, 3, 1]))
    print(sol.pivot_index([1, -1, 4]))