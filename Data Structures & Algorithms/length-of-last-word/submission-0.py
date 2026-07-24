class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        dup_s = s.split()
        return len(dup_s[-1])