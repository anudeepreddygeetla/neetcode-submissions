class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has = {}
        val_1 = []
        for i in nums:
            if i in has:
                has[i] += 1
            else:
                has[i] = 1
        for key , val in has.items():
            val_1.append(val)
        
        for j in val_1:
            if j > 1:
                return True
                break
        return False
