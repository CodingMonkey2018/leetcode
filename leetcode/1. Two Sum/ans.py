class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_len = len(nums)
        sorted_nums = sorted(zip(nums, range(nums_len)),
                             key=lambda t: t[0])
        start, stop = 0, nums_len - 1
        
        while start < stop:
            tmp = sorted_nums[start][0] + sorted_nums[stop][0]
            if tmp < target:
                start += 1
            elif tmp > target:
                stop -= 1
            else:
                return [sorted_nums[start][1], sorted_nums[stop][1]]
        
        return null