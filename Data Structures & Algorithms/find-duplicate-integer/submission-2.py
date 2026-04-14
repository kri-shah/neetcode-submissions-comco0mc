class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for n in nums:
            indx = abs(n)-1
            if nums[indx] < 0:
                return abs(n)
            else:
                nums[indx] *= -1
        