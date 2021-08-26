"""
16. 두 수의 덧셈
2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.


Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:
* The number of nodes in each linked list is in the range [1, 100].
* 0 <= Node.val <= 9
* It is guaranteed that the list represents a number that does not have leading zeros.



"""

# 내 풀이
from typing import Optional

# Definition for singly-linked list.
from pip import __main__


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        sum = 0
        answer_head = answer = ListNode()

        while l1 or l2:
            if not l1:
                print("l1없음")
                s1 = 0
                s2 = l2.val
                l2 = l2.next
            elif not l2:
                print("l2없음")
                s1 = l1.val
                s2 = 0
                l1 = l1.next
            else:
                s1 = l1.val
                s2 = l2.val
                l1 = l1.next
                l2 = l2.next

            carry, sum = divmod((s1 + s2 + carry), 10)
            print(sum)
            answer.next = ListNode(sum)
            answer = answer.next

        # 각 노드의 마지막 값의 합이 10이상 일때 carry 발생
        if carry == 1:
            answer.next = ListNode(carry)

        return answer_head.next

# 풀이 1
# from typing import List
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
#     # 연결 리스트 뒤집기
#     def reverseList(self, head: ListNode) -> ListNode:
#         node, prev = head, None
#
#         while node:
#             next, node.next = node.next, prev
#             prev, node = node, next
#
#         return prev
#
#     # 연결 리스트를 파이썬 리스트로 변환
#     def toList(self, node: ListNode) -> List:
#         list: List = []
#         while node:
#             list.append(node.val)
#             node = node.next
#         return list
#
#     # 파이썬 리스트를 연결 리스트로 변환
#     def toReversedLinkedList(self, result: str) -> ListNode:
#         prev: ListNode = None
#         for r in result:
#             node = ListNode(r)
#             node.next = prev
#             prev = node
#
#         return node
#
#     # 두 연결 리스트의 덧셈
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         a = self.toList(self.reverseList(l1))
#         b = self.toList(self.reverseList(l2))
#
#         resultStr = int(''.join(str(e) for e in a)) + \
#                     int(''.join(str(e) for e in b))
#
#         # 최종 계산 결과 연결 리스트 변환
#         return self.toReversedLinkedList(str(resultStr))


# 풀이 2
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#
# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         root = head = ListNode(0)
#
#         carry = 0
#         while l1 or l2 or carry:
#             sum = 0
#             # 두 입력값의 합 계산
#             if l1:
#                 sum += l1.val
#                 l1 = l1.next
#             if l2:
#                 sum += l2.val
#                 l2 = l2.next
#
#             # 몫(자리올림수)과 나머지(값) 계산
#             carry, val = divmod(sum + carry, 10)
#             head.next = ListNode(val)
#             head = head.next
#
#         return root.next
#


if __name__ == "__main__":
    sol = Solution()
    l1 = ListNode(9, ListNode(9, ListNode(9)))
    l2 = ListNode(9)
    print(sol.addTwoNumbers(l1, l2))
