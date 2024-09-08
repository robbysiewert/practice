from practice import Solution, ListNode

solution = Solution()

def compare_linked_lists(l1: ListNode, l2: ListNode) -> bool:
    while l1 and l2:
        if l1.val != l2.val:
            return False
        l1 = l1.next
        l2 = l2.next
    return l1 is None and l2 is None

def test_twoSum():

    assert solution.twoSum([2, 7, 11, 15], target=9) == [0, 1]
    assert solution.twoSum([3, 2, 4], target=6) == [1, 2]
    assert solution.twoSum([3, 3], target=6) == [0, 1]

def test_addTwoNumbers():

    # Test Case 1
    l1 = ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3)))
    l2 = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4)))
    expected = ListNode(val=7, next=ListNode(val=0, next=ListNode(val=8)))
    result = solution.addTwoNumbers(l1, l2)
    assert compare_linked_lists(result, expected)

    # Test Case 2
    l1 = ListNode(val=0)
    l2 = ListNode(val=0)
    expected = ListNode(val=0)
    result = solution.addTwoNumbers(l1, l2)
    assert compare_linked_lists(result, expected)

    # Test Case 3
    l1 = ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=\
        ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=None)))))))
    l2 = ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9))))
    expected = ListNode(val=8, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next= \
            ListNode(val=0, next=ListNode(val=0, next=ListNode(val=0, next=ListNode(val=1))))))))
    result = solution.addTwoNumbers(l1, l2)
    assert compare_linked_lists(result, expected)

def test_length_of_longest_substring():

    # Test Case 1
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3

    # Test Case 2
    assert solution.lengthOfLongestSubstring("bbbbb") == 1

    # Test Case 3
    assert solution.lengthOfLongestSubstring("pwwkew") == 3

    # Test Case 4
    assert solution.lengthOfLongestSubstring("") == 0

    # Test Case 5
    assert solution.lengthOfLongestSubstring(" ") == 1

    # Test Case 6
    assert solution.lengthOfLongestSubstring("dvdf") == 3

    # Test Case 7
    assert solution.lengthOfLongestSubstring("abba") == 2

    # Test Case 8
    assert solution.lengthOfLongestSubstring("tmmzuxt") == 5

    # Test Case 9
    assert solution.lengthOfLongestSubstring("ohvhjdml") == 6

    # Test Case 10
    assert solution.lengthOfLongestSubstring("aabaab!a") == 3
