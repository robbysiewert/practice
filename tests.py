from practice import Solution, ListNode

def compare_linked_lists(l1: ListNode, l2: ListNode) -> bool:
    while l1 and l2:
        if l1.val != l2.val:
            return False
        l1 = l1.next
        l2 = l2.next
    return l1 is None and l2 is None

def test_twoSum():
    solution = Solution()
    assert solution.twoSum([2, 7, 11, 15], target=9) == [0, 1]
    assert solution.twoSum([3, 2, 4], target=6) == [1, 2]
    assert solution.twoSum([3, 3], target=6) == [0, 1]

def test_addTwoNumbers():
    solution = Solution()

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
