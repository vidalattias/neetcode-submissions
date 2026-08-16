class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []

        for a in asteroids:
            destroyed = False

            while s and (a*s[-1] < 0) and (s[-1]>0) and not destroyed:
                if abs(s[-1]) == abs(a):
                    s.pop()
                    destroyed = True
                elif abs(s[-1]) > abs(a):
                    destroyed = True
                else:
                    s.pop()

            if not destroyed:
                s.append(a)

        return s