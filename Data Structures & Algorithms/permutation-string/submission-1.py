from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        w = len(s1)
        freq_dict_1 = defaultdict(int)
        freq_dict_2 = defaultdict(int)
        if w > len(s2):
            return False
            
        for i in range(w):
            freq_dict_1[s1[i]] += 1
            freq_dict_2[s2[i]] += 1
        
        if freq_dict_1 == freq_dict_2:
            return True
        
        for i in range(w, len(s2)):
            freq_dict_2[s2[i]] += 1
            freq_dict_2[s2[i-w]] -= 1
            if freq_dict_2[s2[i-w]] <= 0:
                del freq_dict_2[s2[i-w]]
            
            if freq_dict_1 == freq_dict_2:
                return True
            

        return False