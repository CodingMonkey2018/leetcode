class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = dict()
        for idx, num in enumerate(nums):
            if num in nums_dict:
                return [idx, nums_dict[num]]
            else:
                nums_dict[target-num] = idx
        return null