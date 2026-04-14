import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        enq = [(e, p, i) for i, (e, p) in enumerate(tasks)]
        heapq.heapify(enq)
        
        res = []
        proc_q = []
        time = enq[0][0]
        while enq or proc_q:
            while enq and enq[0][0] <= time:
                e, p, i = heapq.heappop(enq)
                heapq.heappush(proc_q, (p, i))
            
            if not proc_q:
                time = enq[0][0]
                continue

            p, i = heapq.heappop(proc_q)
            time += p
            res.append(i)
        
        return res
            