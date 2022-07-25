class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Init a set to keep track of what we've seen already
        history = set()

        # Going through each number and adding them as we go
        for num in nums:
            if num in history:
                return True
            history.add(num)
        return False