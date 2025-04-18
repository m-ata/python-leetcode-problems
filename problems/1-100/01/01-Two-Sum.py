from typing import List

class Solution:
	def twoSum(self, nums, target):
		mapping = {}

		for index, val in enumerate(nums):
			diff = target - val
			if diff in mapping:
				return [index, mapping[diff]]
			else:
				mapping[val] = index


solution = Solution()
print(solution.twoSum([2,7,11,15], 9))