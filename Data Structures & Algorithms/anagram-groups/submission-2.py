class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        def anagram(s):
            arr = [0] * 26
            for c in s:
                arr[ord(c) - ord('a')] += 1
            return tuple(arr)
        
        for s in strs:
            groups[anagram(s)].append(s)
        
        res = [value for value in groups.values()]
        return res