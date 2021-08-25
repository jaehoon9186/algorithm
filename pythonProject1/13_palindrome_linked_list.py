"""
13. 팰린드롬 연결 리스트
234. Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/

Given the head of a singly linked list, return true if it is a palindrome.


Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false


Constraints:
The number of nodes in the list is in the range [1, 10**5].
0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?
"""
# 내풀이
# pass

# 풀이 1
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q: List = []

        if not head:
            return True

        node = head
        # 리스트 변환
        while node is not None:
            q.append(node.val)
            node = node.next


        # 팰린드롬 판별
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False

        return True

# 풀이 2 #input이 좀 다름
# import collections
# from typing import Deque
#
#
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#
# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:
#         # 데크 자료형 선언
#         q: Deque = collections.deque()
#
#         if not head:
#             return True
#
#         node = head
#         while node is not None:
#             q.append(node.val)
#             node = node.next
#
#         while len(q) > 1:
#             if q.popleft() != q.pop():
#                 return False
#
#         return True

# 풀이 4
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#
# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:
#         rev = None
#         slow = fast = head
#         # 런너를 이용해 역순 연결 리스트 구성
#         while fast and fast.next:
#             fast = fast.next.next
#             rev, rev.next, slow = slow, rev, slow.next
#         if fast:
#             slow = slow.next
#
#         # 팰린드롬 여부 확인
#         while rev and rev.val == slow.val:
#             slow, rev = slow.next, rev.next
#         return not rev

if __name__=="__main__":
    sol = Solution()
    head = ListNode(1,ListNode(2, ListNode(2, ListNode(1, None))))
    print(sol.isPalindrome(head))
