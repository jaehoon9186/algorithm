"""
18. 홀짝 연결 리스트
328. Odd Even Linked List
https://leetcode.com/problems/odd-even-linked-list/

Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
The first node is considered odd, and the second node is even, and so on.
Note that the relative order inside both the even and odd groups should remain as it was in the input.
You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Example 1:
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]


Constraints:
* n == number of nodes in the linked list
* 0 <= n <= 10**4
* -10**6 <= Node.val <= 10**6

"""

# 내 풀이
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return None

        root = head
        even_first = head.next
        count = 1
        while head:
            if count % 2 == 1:  # 홀수
                if not head.next or not head.next.next:
                    head.next = even_first
                    break

            temp = head.next
            head.next = temp.next
            head = temp

            count += 1

        return root

# 풀이 1
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#
# class Solution:
#     def oddEvenList(self, head: ListNode) -> ListNode:
#         # 예외 처리
#         if head is None:
#             return None
#
#         odd = head
#         even = head.next
#         even_head = head.next
#
#         # 반복하면서 홀짝 노드 처리
#         while even and even.next:
#             odd.next, even.next = odd.next.next, even.next.next
#             odd, even = odd.next, even.next
#
#         # 홀수 노드의 마지막을 짝수 헤드로 연결
#         odd.next = even_head
#         return head

if __name__ == "__main__":
    sol = Solution()
    # head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    head = ListNode()
    print(sol.oddEvenList(head))
