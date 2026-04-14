class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        '''
        [1,2,4,2,3,5,3,4]

        '''
        if len(hand) % groupSize != 0:
            return False
        
        freq_dict = dict()
        for h in hand:
            freq_dict[h] = freq_dict.get(h, 0) + 1
        
        hand.sort()
        for key in hand:
            if freq_dict.get(key, 0) == 0:
                continue
            for i in range(groupSize):
                if freq_dict.get(key + i, 0) <= 0:
                    return False
                else:
                    freq_dict[key + i] -= 1
        
        return True