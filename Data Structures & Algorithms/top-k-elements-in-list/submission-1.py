class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq =[[] for i in range(len(nums) + 1) ] #number of buckets, max freq = len + 1
        # each bucket is the num which has i frequency

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n)  #put the values with c frequency into each bucket

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)

                if len(res) == k: 
                    return res