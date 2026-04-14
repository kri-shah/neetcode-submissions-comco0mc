from collections import defaultdict
class TimeMap:
    def __init__(self):
        self.time_dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_dict[key].append([timestamp, value])
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_dict:
            return ""
        
        arr = self.time_dict[key]
        print(arr)

        l = 0
        r = len(arr)-1
        res = ""
        while l <= r:
            m = l+(r-l)//2
            if arr[m][0] <= timestamp:
                res = arr[m][1]
                l = m+1
            else:
                r = m-1
                
            
        return res 

