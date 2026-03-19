"""Find the Duplicate Number
Medium
Topics
Company Tags
Hints
You are given an array of integers nums containing n + 1 integers. Each integer in nums is in the range [1, n] inclusive.

Every integer appears exactly once, except for one integer which appears two or more times. Return the integer that appears more than once.
"""

from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        idx = 0
        slow = nums[idx]
        fast = nums[nums[idx]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
