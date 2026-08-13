class Solution:
    def isPalindrome(self, s: str) -> bool:
        sl = s.lower()
        s = []
        for x in sl:
            if x in 'qwertyuiopasdfghjklzxcvbnm1234567890':
                s.append(x)


        print(f'New s -> {s}')
        N = len(s)

        for i in range(N//2):
            if s[i] != s[N-i-1]:
                return False
        return True