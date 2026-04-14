from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()  # stores indices, values are decreasing

        # build first window
        for i in range(k):
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)

        res = [nums[q[0]]]

        # slide
        for i in range(k, len(nums)):
            # remove indices that are left of the window
            while q and q[0] <= i - k:
                q.popleft()

            while q and nums[q[-1]] <= nums[i]:
                q.pop()

            q.append(i)
            res.append(nums[q[0]])

        return res
