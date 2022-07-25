class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ans = False
        if len(s) != len(t):
            ans = False
            
        Dict = dict()
        Dict2 = dict()
        
        for letter in s:
            if letter not in t:
                ans = False
                
            if letter in Dict:
                Dict[letter] += 1
            else:
                Dict[letter] = 1
                
        for letter in t:
            if letter in Dict2:
                Dict2[letter] += 1
            else:
                Dict2[letter] = 1
                
        if Dict == Dict2:
            ans = True
    
        return ans