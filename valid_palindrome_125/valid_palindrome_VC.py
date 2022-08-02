class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = True
        if len(s) == 1:
            return True
        temp_str = ""
        for i in s:
            if i.isalnum():
                temp_str += i
        temp_str = temp_str.lower()

        half = len(temp_str)//2
        for i in range(0, half):
            if (temp_str[i] == temp_str[len(temp_str)-i-1]):
                ans = True
            else: 
                ans = False
                break
        return ans