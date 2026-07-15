class Solution(object):
    def topKFrequent(self, nums, k):
        #hello
        count={}
        freq=[[] for i in range(len(nums)+1)]
        for n in nums:
            count[n]=count.get(n,0)+1
        for c,v in count.items():
            freq[v].append(c)
        res=[]
        for i in range(len(nums),0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res