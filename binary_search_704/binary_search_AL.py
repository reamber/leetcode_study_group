class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        l = 0
        r = len(nums) - 1
        while(l <= r): #while the left and right index dont touch
            mid = (l + r) / 2 #midpoint formula
            if nums[mid] == target: #if the middle is the value we are searching for, return mid ind
                return mid
            elif nums[mid] < target: #if its less then, we have to update our left ind
                l = mid + 1    
            else:
                r = mid - 1 #same but if its bigger than target
        return -1
