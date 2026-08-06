class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        w1 = [0] * 26
        w2 = [0] * 26
        for i in range(len(s)):
            w1[ord(s[i]) - ord('a')] += 1
            w2[ord(t[i]) - ord('a')] += 1

        return w1 == w2
         
            