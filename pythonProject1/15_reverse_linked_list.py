"""
15 역순 연결 리스트
206. reverse linked list
https://leetcode.com/problems/reverse-linked-list/

Given the head of a singly linked list, reverse the list, and return the reversed list.


Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []


Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000


Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

"""

# 내 풀이
# from typing import Optional
#
#
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         rev = None
#
#         while head:
#             rev, rev.next, head = head, rev,head.next
#
#         return rev




# 내 풀이 2
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp


        return prev





# 풀이 1
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         def reverse(node: ListNode, prev: ListNode = None):
#             if not node:
#                 return prev
#             next, node.next = node.next, prev
#             return reverse(next, node)
#
#         return reverse(head)

# 풀이 2
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         node, prev = head, None
#
#         while node:
#             next, node.next = node.next, prev
#             prev, node = node, next
#
#         return prev


if __name__ == "__main__":
    sol = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
    print(sol.reverseList(head))
