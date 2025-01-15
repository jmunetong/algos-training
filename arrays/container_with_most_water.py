class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_idx = 0
        right_idx = len(height)-1
        max_area = min(height[left_idx], height[right_idx]) * (right_idx -  left_idx)
        
        while left_idx < right_idx:
            if height[left_idx] < height[right_idx]:
                left_idx +=1
            else:
                right_idx -=1
        
            max_area =  max(min(height[left_idx], height[right_idx]) * (right_idx  -  left_idx), max_area)
 
        return max_area

                
            


        