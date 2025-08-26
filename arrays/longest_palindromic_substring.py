
### Brute force approach o(n^3)
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n <=1:
            return s
        max_len = 0
        str_cum = ""
        for i in range(n):
            for j in range(i+1, n+1):
                if s[i:j] == s[i:j][::-1] and (j-i)  >= max_len:
                    max_len = j-i 
                    str_cum = s[i:j]
        return  str_cum




                


        