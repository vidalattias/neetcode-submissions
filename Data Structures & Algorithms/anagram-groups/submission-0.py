class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = {}
        for s in strs:
            h = str(sorted(s))
            if h not in ret:
                ret[h] = []
            ret[h].append(s)
        return [ret[h] for h in ret]