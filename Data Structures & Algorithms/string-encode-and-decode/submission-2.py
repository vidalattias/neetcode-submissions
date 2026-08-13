delimiter = '+'
wrapping = '-'

class Solution:
    def encode(self, strs: List[str]) -> str:
        ret = ''
        for s in strs:
            ret += str(len(s)) + '#' + s
        return ret

    def decode(self, s: str) -> List[str]:
        index = 0
        ret = []
        N = len(s)
        while(index<N):
            length = s[index:].split('#')[0]
            length_nb_chars = len(length)
            length_int = int(length)
            index_start = index+length_nb_chars+1
            index_end = index+length_nb_chars+1+length_int
            encoded_str = s[index_start:index_end]

            index = index_end

            ret.append(encoded_str)
        return ret

