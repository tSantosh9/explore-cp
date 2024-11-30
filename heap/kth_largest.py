# Link: https://leetcode.com/problems/kth-largest-element-in-an-array/
from queue import PriorityQueue
from typing import List


class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        pqueue = PriorityQueue()
        for i in range(k):
            pqueue.put(nums[i])
        index = pqueue.qsize()
        for i in range(index, len(nums)):
            if nums[i] > pqueue.queue[0]:
                pqueue.get()
                pqueue.put(nums[i])
        return pqueue.get()

if __name__ == '__main__':
    solution = Solution()
    print(solution.findKthLargest([3, 2, 1, 5, 6, 4], 2))  # 5
    print(solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 4
    print(solution.findKthLargest([3, 2, 1, 5, 6, 4], 2))  # 5
    print(solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 4
    print(solution.findKthLargest([3, 2, 1, 5, 6, 4], 2))  # 5
    print(solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 4
    print(solution.findKthLargest([3, 2, 1, 5, 6, 4], 2))  # 5
    print(solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 4
    print(solution.findKthLargest([3, 2, 1, 5, 6, 4], 2))  # 5
    print(solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 4
    print(solution.findKthLargest([3, 2, 1, 5, 6, 4], 2))  # 5
    print(solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 4
    print(solution.findKthLargest([3, 2, 1, 5, 6, 4], 2))