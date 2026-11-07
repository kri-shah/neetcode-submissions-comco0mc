class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        pivot = l
        def bin_search(l, r):
            while l <= r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m +1
                elif nums[m] > target:
                    r = m - 1
                else:
                    return m
            return -1
        

        left = bin_search(0, pivot - 1)
        right = bin_search(pivot, len(nums) - 1)
        
        if left != -1:
            return left
        if right != -1:
            return right
        
        return -1


        