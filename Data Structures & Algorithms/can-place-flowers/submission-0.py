class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Loop through each plot in the flowerbed
        for i in range(len(flowerbed)):
            # Check if current plot, previous plot, and next plot are all empty (or boundaries)
            if flowerbed[i] == 0:
                left_empty = (i == 0) or (flowerbed[i - 1] == 0)
                right_empty = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                
                if left_empty and right_empty:
                    flowerbed[i] = 1  # Plant a flower
                    n -= 1            # Decrease required flowers
                    
            # Early exit if all flowers are successfully planted
            if n <= 0:
                return True
                
        return n <= 0
