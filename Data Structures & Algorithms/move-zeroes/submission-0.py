class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        insert = 0
        for num in nums:
            if num != 0:
                nums[insert] = num
                insert += 1
        while insert < len(nums):
            nums[insert] = 0
            insert += 1
        
        