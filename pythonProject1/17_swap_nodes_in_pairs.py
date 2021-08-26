"""
17. 페어의 노드 스왑
24. Swap Nodes in Pairs
https://leetcode.com/problems/swap-nodes-in-pairs/

Given a linked list, swap every two adjacent nodes and return its head.
You must solve the problem without modifying the values in the list's nodes
(i.e., only nodes themselves may be changed.)


Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]


Constraints:
* The number of nodes in the list is in the range [0, 100].
* 0 <= Node.val <= 100

"""
# 내 풀이
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = prev = curr = ListNode(None, head)
        curr = curr.next

        while curr and curr.next:
            # None(prev) -> 2(curr) -> 1 -> 4 -> 3 -> None
            temp = curr.next  # None(prev) -> 2(curr) -> 1(temp) -> 4 -> 3 -> None
            curr.next = temp.next  # None(prev) -> 2(curr) -> 4   1(temp) -> 4 -> 3 -> None
            temp.next = curr # None(prev) -> 2(curr) -> 4  1(temp) -> 2 -> 4 -> 3 -> None

            prev.next = temp
            # None(prev) -> 1(temp) -> 2(curr) -> 4 -> 3 -> None

            curr = curr.next
            prev = prev.next.next
            # None -> 1 -> 2(prev) -> 4(curr) -> 3 -> None


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
#     def swapPairs(self, head: ListNode) -> ListNode:
#         cur = head
#
#         while cur and cur.next:
#             # 값만 교환
#             cur.val, cur.next.val = cur.next.val, cur.val
#             cur = cur.next.next
#
#         return head


# 풀이 2
#
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#
# class Solution:
#     def swapPairs(self, head: ListNode) -> ListNode:
#         root = prev = ListNode(None)
#         prev.next = head
#         while head and head.next:
#             # b가 a(head)를 가리키도록
#             b = head.next
#             head.next = b.next
#             b.next = head
#
#             # prev가 b를 가리키도록
#             prev.next = b
#
#             # 다음 번 비교를 위해 이동
#             head = head.next
#             prev = prev.next.next
#         return root.next

# 풀이 3
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#
# class Solution:
#     def swapPairs(self, head: ListNode) -> ListNode:
#         if head and head.next:
#             p = head.next
#             # 스왑된 값 리턴 받음
#             head.next = self.swapPairs(p.next)
#             p.next = head
#             return p
#         return head




if __name__ == "__main__":
    sol = Solution()
    head = ListNode(2, ListNode(1, ListNode(4, ListNode(3))))
    print(sol.swapPairs(head))
