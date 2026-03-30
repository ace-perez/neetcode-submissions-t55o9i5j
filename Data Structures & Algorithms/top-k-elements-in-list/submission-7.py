from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for _ in range(len(nums)+1)]

        for i in nums:
            count[i] += 1

        for i, c in count.items():
            freq[c].append(i)

        res = []
        for i in range(len(nums),0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res




        