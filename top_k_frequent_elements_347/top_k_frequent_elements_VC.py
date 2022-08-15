class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        #get all frequencies
        for num in nums:
            if num in freq:
                freq[num] +=1
            else:
                freq[num] = 1
        print(freq)
        #sort frequencies & reversed
        sortedFreq = sorted(freq,key=freq.get,reverse=True)
        ans = []
        #append first k elements to ans array
        for i in range(0, k):
            ans.append(sortedFreq[i])
        print(sortedFreq)
        return ans