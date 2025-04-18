from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, num in enumerate(nums):
            if nums[index] + nums[index+1] == target:
                return [index, index+1]


solution = Solution()
print(solution.twoSum([2,7,11,15], 9))