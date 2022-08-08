class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        num_set = set(nums) #remove the duplicate vals and also make each val accessible
        
        max_so_far = 0
        
        for n in num_set:
            if(n-1) not in num_set:
                length = 0
                while(n+length) in num_set: #think as n, n+1, n+2 to check if consecutive num is in the set
                    length += 1
                
                max_so_far = max(max_so_far, length)
        
        return max_so_far
