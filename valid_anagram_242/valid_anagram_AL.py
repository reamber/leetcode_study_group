class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        #base case, if length of the two strings are not equal it can't be an anagram
        if len(s) != len(t): 
            return False
        
        tracker = {} #key would be the letter, value would be the counter
        
        for char in s:
            if char in tracker:
                tracker[char] += 1 #if it's in the dict already, increase vounter
            else:
                tracker[char] = 1 #if not, initialize key value
                
        for char in t: #check if characters in t is the same as s
            if char not in tracker: #if it differs return false
                return False
            else:
                tracker[char] -= 1 #subtrack the counter, the value should be 0 if t has the exact same letters as s
        
        for k, v in tracker.items():
            if v != 0:
                return False
        return True
            
            
            
            
        
