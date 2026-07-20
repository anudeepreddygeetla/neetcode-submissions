class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for st in strs:
            count = [0] * 26

            for c in st:
                count[ord(c) - ord('a')] += 1
            clean_key = tuple(count)
            if clean_key not in result:
                result[clean_key] = []
            
            result[clean_key].append(st)

        return list(result.values())
        

            


        