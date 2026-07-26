class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        final_count = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                if count > final_count:
                    final_count = count
                count = 0
        if count > final_count:
            return count
        else:
            return final_count
        