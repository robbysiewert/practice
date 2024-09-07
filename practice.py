# LeetCode Solutions

from typing import List

class Solution:

    def __init__(self) -> None:
        pass


    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            else:
                num_map[num] = i
        return []

    def test_twoSum(self):
        assert self.twoSum([2, 7, 11, 15], 9) == [0, 1]
        print("All tests passed!")

test_solution = Solution()
test_solution.test_twoSum()