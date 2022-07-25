class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        history = {}
        
        # Populate history with character counts
        for char in s:
            if char in history:
                history[char] += 1
            else:
                history[char] = 1
        
        # Decrement character count as we see them
        for char in t:
            if char in history:
                history[char] -= 1
            else:
                # Return False if we see an unrecognized character
                return False
        # Get all values portion of dictionary
        char_counts = history.values()
        
        # Check all to see if equal to 0
        return all(c == 0 for c in char_counts)