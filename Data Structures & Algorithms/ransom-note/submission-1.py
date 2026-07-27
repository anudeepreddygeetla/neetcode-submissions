class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
      char_counts = Counter(magazine)
        
        # Check each character in the ransom note
      for char in ransomNote:
        if char_counts[char] <= 0:
            return False
        char_counts[char] -= 1
            
      return True  