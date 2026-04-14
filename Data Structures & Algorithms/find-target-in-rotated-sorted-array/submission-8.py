class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        m = -1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        piv = l
        def bin_search(l, r):
            while l <= r:
                m = (l + r) // 2
                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    return m
            return -1
        
        
        l, r = 0, len(nums) - 1
        
        res = -1
        if target >= nums[piv] and target <= nums[-1]:
            res = bin_search(piv, r)
        else:
            res = bin_search(l, piv - 1)
        
        return res


