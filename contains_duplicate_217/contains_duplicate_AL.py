class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        #input: nums -> int array, []
        #output: boolean, true or false
        
        #use a set and compare the size of that set to the [], if not equal there is a duplicate, return true
        
        #else return false
        
        to_set = set(nums)
        
        if len(to_set) != len(nums):
            return True
        else:
            return False
        
        
        
