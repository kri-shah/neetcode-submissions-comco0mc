class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0 
        r = len(matrix) - 1
        arr = []
        while l <= r: 
            mid = l + (r - l) // 2
            print(mid)
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                arr = matrix[mid]
                break
            elif matrix[mid][0] > target:
                r = mid -1
            else:
                l = mid + 1
        print(arr)
        if not arr:
            return False
        
        l = 0
        r = len(arr) - 1
        while l <= r: 
            mid = l + (r - l) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False