class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1counter = Counter(s1)
        windowCount = Counter()

        l = 0
        for  r in range(len(s2)):

            windowCount[s2[r]] += 1
            if r-l+1 > len(s1):
                windowCount[s2[l]] -= 1
                if windowCount[s2[l]] == 0:
                    del windowCount[s2[l]]
                l += 1

            if s1counter == windowCount:
                return True
        return False
        