class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for cust in details:
            age = int(str(cust[11]) + str(cust[12]))
            if age > 60:
                count += 1
        return count