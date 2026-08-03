class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        arrange = {}
        for h , n in zip(heights , names):
            arrange[h] = n
        res = []
        for h in reversed(sorted(heights)):
            res.append(arrange[h])
        return res
                




        