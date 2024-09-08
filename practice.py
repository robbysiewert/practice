# LeetCode Solutions

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    # Problem 1
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            else:
                num_map[num] = i
        return []

    # Problem 2
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry_the_one = 0
        head = current = ListNode(0)
        while l1 or l2 or carry_the_one:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            val_sum = val1 + val2 + carry_the_one
            carry_the_one = val_sum // 10
            current.next = ListNode(val=val_sum % 10, next=None)
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head.next

    # Problem 3
    def lengthOfLongestSubstring(self, s: str) -> int:

        # initialize variables
        len_longest_substring = 0
        current_substring = ''

        for element in s:
            if element in current_substring: # Handle repeated elements
                # Cut the first part of the substring off, including the first appearance of the repeated element
                current_substring = current_substring[current_substring.index(element) + 1:]
            current_substring = current_substring + element # Append element - if repeat, the repeated piece has been cut off already
            # if the current substring is longest, save it to be either beaten later in the loop or returned
            len_current_substring = len(current_substring)
            if len_current_substring > len_longest_substring:
                len_longest_substring = len_current_substring
        return len_longest_substring

    # Problem 4
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combined_array = nums1 + nums2
        combined_array.sort()
        median_index = len(combined_array) // 2
        if len(combined_array) % 2 != 0:
            return float(combined_array[median_index])
        else:
            return (combined_array[median_index] + combined_array[median_index - 1]) / 2