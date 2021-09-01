"""
27. k개 정렬 리스트 병합
23. merge k sorted lists
https://leetcode.com/problems/merge-k-sorted-lists/


You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.


Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []


Constraints:
* k == lists.length
* 0 <= k <= 10^4
* 0 <= lists[i].length <= 500
* -10^4 <= lists[i][j] <= 10^4
* lists[i] is sorted in ascending order.
* The sum of lists[i].length won't exceed 10^4.

"""

# 내 풀이 브루트포스
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for nlist in lists:
            while nlist:
                arr.append(nlist.val)
                nlist = nlist.next
        print(arr)

        head = curr = None

        for val in sorted(arr):
            if not curr:
                head = curr = ListNode(val)
            else:
                curr.next = ListNode(val)
                curr = curr.next


        return head

# 풀이 1
# import heapq
# from typing import List
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#
# class Solution:
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         root = result = ListNode(None)
#         heap = []
#
#         # 각 연결 리스트의 루트를 힙에 저장
#         for i in range(len(lists)):
#             if lists[i]:
#                 heapq.heappush(heap, (lists[i].val, i, lists[i]))
#
#         # 힙 추출 이후 다음 노드는 다시 저장
#         while heap:
#             node = heapq.heappop(heap)
#             idx = node[1]
#             result.next = node[2]
#
#             result = result.next
#             if result.next:
#                 heapq.heappush(heap, (result.next.val, idx, result.next))
#
#         return root.next


if __name__ == "__main__":
    sol = Solution()

    # lists = ListNode(ListNode(1,ListNode(4,ListNode(5))), ListNode(ListNode(1,ListNode(3,ListNode(4))), ListNode(ListNode(2,ListNode(6)))) )

    lists = ListNode(ListNode(1,ListNode(4,ListNode(5))))
    lists.next = ListNode(ListNode(1,ListNode(3,ListNode(4))))
    lists.next.next = ListNode(ListNode(2,ListNode(6)))

    print(sol.mergeKLists(lists))