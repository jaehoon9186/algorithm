"""
14. 두 정렬 리스트의 병합
21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/

Merge two sorted linked lists and return it as a sorted list.
The list should be made by splicing together the nodes of the first two lists.


Example 1:
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: l1 = [], l2 = []
Output: []

Example 3:
Input: l1 = [], l2 = [0]
Output: [0]


Constraints:
* The number of nodes in both lists is in the range [0, 50].
* -100 <= Node.val <= 100
* Both l1 and l2 are sorted in non-decreasing order.

"""

# 내 풀이
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        root = answer = ListNode()

        # 예외 처리 l1, l2 값이 없을때 or 둘 중 하나의 리스트의 값이 없을때
        if not l1 and not l2:
            print("둘다 없음 ")
            return root.next


        while l1 or l2:
            # l1 l2가 존재하지 않을경우
            if not l1 :
                value = l2.val
                l2 = l2.next
            elif not l2:
                value = l1.val
                l1 = l1.next

            # l1, l2가 존재하는 경우 or 비교
            if l1 and l2:
                if l1.val < l2.val:
                    value = l1.val
                    l1 = l1.next
                elif l1.val >= l2.val:
                    value = l2.val
                    l2 = l2.next

            answer.next = ListNode(value)
            answer = answer.next

        return root.next



# 풀이 1
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#
# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         if (not l1) or (l2 and l1.val > l2.val):
#             l1, l2 = l2, l1
#         if l1:
#             l1.next = self.mergeTwoLists(l1.next, l2)
#         return l1

if __name__ == "__main__":
    sol = Solution()
    # l1 = ListNode(1, ListNode(2, ListNode(4, None)))
    # l2 = ListNode(1, ListNode(3, ListNode(4, None)))
    l1 = None
    l2 = ListNode()
    print(sol.mergeTwoLists(l1, l2))
