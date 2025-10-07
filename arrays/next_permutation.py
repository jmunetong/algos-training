class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1) Need to find pivot: last_position_num > ith_position_num (n-2, n-3, ...)
        # 2) Swap the elements in the found indeces
        # 3) anything beyond index ith_position (position) needs to be sorted in ascending order

        N = len(nums)
        i = N-1
        j = i - 1
        while j >=0 and nums[j] >= nums[i]:
            i-=1
            j -=1
        pivot = j
        i = N -1
        if pivot >=0:
            while nums[i] <= nums[pivot]:
                i -=1
            nums[i], nums[pivot] = nums[pivot], nums[i]
        k = pivot + 1
        i = N-1
  
        while k < i:
            if nums[k] > nums[i]:
                nums[i], nums[k] = nums[k], nums[i]
            k +=1
            i -= 1 


