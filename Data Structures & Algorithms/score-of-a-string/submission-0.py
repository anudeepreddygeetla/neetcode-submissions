class Solution:
    def scoreOfString(self, s: str) -> int:
        out = 0
        for i in range(len(s) - 1):
            out += abs(ord(s[i + 1]) - ord(s[i]))
        return out

        