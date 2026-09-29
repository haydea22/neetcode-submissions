class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        h = {}
        for ch in s:
            h[ch] = h.get(ch, 0) + 1
        for ch in t:
            if h.get(ch, 0) == 0:
                return False
            h[ch] -= 1
        return True