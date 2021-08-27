"""
19. 역순 연결 리스트 II
92. Reverse Linked List II
https://leetcode.com/problems/reverse-linked-list-ii/

Given the head of a singly linked list and two integers left and right where left <= right,
reverse the nodes of the list from position left to position right, and return the reversed list.


Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]


Constraints:
* The number of nodes in the list is n.
* 1 <= n <= 500
* -500 <= Node.val <= 500
* 1 <= left <= right <= n


Follow up: Could you do it in one pass?

"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        root = start = ListNode(None, head)

        for _ in range(left-1):
            start = start.next

        end = start.next

        for _ in range(right - left):
            temp = end.next
            end.next = temp.next
            temp.next = start.next
            start.next = temp


        return root.next

# 풀이 1
#
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#
# class Solution:
#     def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
#         # 예외 처리
#         if not head or m == n:
#             return head
#
#         root = start = ListNode(None)
#         root.next = head
#         # start, end 지정
#         for _ in range(m - 1):
#             start = start.next
#         end = start.next
#
#         # 반복하면서 노드 차례대로 뒤집기
#         for _ in range(n - m):
#             tmp, start.next, end.next = start.next, end.next, end.next.next
#             start.next.next = tmp
#         return root.next


if __name__ == "__main__":
    sol = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    left = 2
    right = 4
    print(sol.reverseBetween(head, left, right))
