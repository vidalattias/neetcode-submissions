import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for elt in nums:
            count[elt] += 1
        
        heap = []

        for elt in count:
            heapq.heappush(heap, (count[elt], elt))
            if len(heap) > k:
                heapq.heappop(heap)

        return [y for (_,y) in heap]