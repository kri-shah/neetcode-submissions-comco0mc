class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        
        shift = l
        
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l+(r-l)//2
            shifted_mid = (mid + shift) % len(nums)
            if nums[shifted_mid] == target:
                return shifted_mid
            elif nums[shifted_mid] > target:
                r = mid - 1
            else:
                l = mid + 1
    
        
        return -1