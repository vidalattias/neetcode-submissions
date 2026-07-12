from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        count = defaultdict(int)
        for elt in nums:
            count[elt] += 1
        
        buckets = [[] for _ in range(n+1)]

        for elt in count:
            print(f'{elt=}')
            print(f'{count[elt]=}')
            buckets[count[elt]].append(elt)
            print(f'{buckets}')
            print()


        print()
        print(f'{count=}')
        print(f'{buckets=}')

        candidates = []
        for i in range(1, n+1)[::-1]:
            if buckets[i] != []:
                candidates += buckets[i]
            if len(candidates) >= k:
                break

        return candidates