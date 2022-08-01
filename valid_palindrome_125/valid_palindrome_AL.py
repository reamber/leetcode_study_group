class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 1:
            return True

        temp = '' 
        for i in s: 
            if i.isalnum(): 
                temp += i.lower()
        print(temp)        
        print(temp[::-1])
        return temp == temp[::-1]
        
     
        
