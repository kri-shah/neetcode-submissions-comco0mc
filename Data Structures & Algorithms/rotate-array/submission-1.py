class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        temp = []
        for i in range(n - k, n):
            temp.append(nums[i])
        
        for i in range(n - k):
            temp.append(nums[i])
        
        nums[:] = temp