class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        has = {}
        m = len(nums)/2
        for i in nums:
            if i in has:
                has[i] += 1
            else:
                has[i] = 1
        for key,val in has.items():
            if val > m:
                return key
        