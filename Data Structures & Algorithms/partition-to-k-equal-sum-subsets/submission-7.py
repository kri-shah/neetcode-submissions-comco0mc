class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        num_sum = sum(nums)
        if num_sum % k != 0:
            return False
        
        nums.sort(reverse=True)
        target = num_sum / k
        used = set()
        def backtrack(indx, s, k):
            if k == 1:
                return True
            if s > target:
                return False

            for i in range(indx, len(nums)):
                if i in used:
                    continue
                if s + nums[i] == target:
                    used.add(i)
                    if backtrack(0, 0, k - 1):
                        return True
                    used.remove(i)
                else:
                    used.add(i)
                    if backtrack(i + 1, s + nums[i], k):
                        return True
                    used.remove(i)
                
                if s == 0:
                    return False

            return False

        return backtrack(0, 0, k)