class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count = (len(nums))/2
        
        num_map = {}
        
        for n in nums:
            if n in num_map:
                num_map[n] += 1
            else:
                num_map[n] = 1
        
        for k, v in num_map.items():
            if v > count:
                return k
            
