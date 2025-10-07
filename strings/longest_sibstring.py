
from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_set = 0
        i = 0
        j = i
        counter = Counter()
        n = len(s)
        while j < n:
                counter[s[j]] +=1
                while counter[s[j]] > 1:
                    counter[s[i]] -=1
                    i += 1
                max_set = max(max_set, j-i + 1)
                j += 1
        return max_set


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = ''
        max_count =0
        for e in s:
            if e not in sub:
                sub += e
                max_count = max(max_count, len(sub))
            else:
                cuts = sub.split(e)[-1]
                sub = cuts + e
        return max_count

            

            
            


