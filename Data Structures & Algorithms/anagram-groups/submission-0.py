from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for r in s:
                count[ord(r) - ord('a')] += 1
            
            res[tuple(count)].append(s)

        return list(res.values())
        