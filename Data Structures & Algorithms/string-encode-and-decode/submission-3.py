delimiter = '+'
wrapping = '-'

class Solution:
    def encode(self, strs: List[str]) -> str:
        ret = ''
        for s in strs:
            ret += f'{len(s)}#{s}'
        return ret

    def decode(self, s: str) -> List[str]:
        ret = []
        i = 0
        N = len(s)
        
        while i < N:
            l_str = s[i:].split('#')[0]
            len_l = len(l_str)
            l = int(l_str)

            i_start = i + len_l + 1
            i_end = i + len_l + 1 + l

            og_s = s[i_start:i_end]
            ret.append(og_s)
            i = i_end

        return ret
