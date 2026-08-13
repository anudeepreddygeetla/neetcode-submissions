class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                ans = mid       # Save mid as a possible answer
                left = mid + 1  # Search the upper/larger half
            else:
                right = mid - 1 # Search the lower/smaller half
                
        return ans
