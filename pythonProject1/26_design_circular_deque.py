"""
26. 원형 데크 디자인
641. Design Circular Deque
https://leetcode.com/problems/design-circular-deque/

Design your implementation of the circular double-ended queue (deque).

Implement the MyCircularDeque class:
* MyCircularDeque(int k) Initializes the deque with a maximum size of k.
* boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise.
* boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise.
* boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise.
* boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise.
* int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
* int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
* boolean isEmpty() Returns true if the deque is empty, or false otherwise.
* boolean isFull() Returns true if the deque is full, or false otherwise.


Example 1:
Input
["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 2, true, true, true, 4]

Explanation
MyCircularDeque myCircularDeque = new MyCircularDeque(3);
myCircularDeque.insertLast(1);  // return True
myCircularDeque.insertLast(2);  // return True
myCircularDeque.insertFront(3); // return True
myCircularDeque.insertFront(4); // return False, the queue is full.
myCircularDeque.getRear();      // return 2
myCircularDeque.isFull();       // return True
myCircularDeque.deleteLast();   // return True
myCircularDeque.insertFront(4); // return True
myCircularDeque.getFront();     // return 4


Constraints:
* 1 <= k <= 1000
* 0 <= value <= 1000
* At most 2000 calls will be made to insertFront, insertLast, deleteFront, deleteLast, getFront, getRear, isEmpty, isFull.
"""

# 내 풀이  # 문제가 데크로 만들면 안되는건지..
import collections


class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.deque = collections.deque([None]*k)
        self.maxlan = k
        self.front = 0
        self.rear = 0

        print(self.deque)
        print(self.isEmpty())

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if not self.isFull():
            self.front = (self.front - 1) % self.maxlan
            self.deque[self.front] = value

            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if not self.isFull():
            self.deque[self.rear] = value
            self.rear = (self.rear + 1) % self.maxlan
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.deque[self.front] is not None:
            self.deque[self.front] = None
            self.front = (self.front+1) % self.maxlan
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.deque[(self.rear-1) % self.maxlan] is not None:
            self.rear = (self.rear - 1) % self.maxlan
            self.deque[self.rear] = None
            return True
        else:
            return False

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        else:
            return self.deque[self.front]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        else:
            return self.deque[(self.rear-1) % self.maxlan]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.front == self.rear and self.deque[self.front] is None

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.front == self.rear and self.deque[self.front] is not None

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()

# 풀이 1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#
# class MyCircularDeque:
#     def __init__(self, k: int):
#         self.head, self.tail = ListNode(None), ListNode(None)
#         self.k, self.len = k, 0
#         self.head.right, self.tail.left = self.tail, self.head
#
#     # 이중 연결 리스트에 신규 노드 삽입
#     def _add(self, node: ListNode, new: ListNode):
#         n = node.right
#         node.right = new
#         new.left, new.right = node, n
#         n.left = new
#
#     def _del(self, node: ListNode):
#         n = node.right.right
#         node.right = n
#         n.left = node
#
#     def insertFront(self, value: int) -> bool:
#         if self.len == self.k:
#             return False
#         self.len += 1
#         self._add(self.head, ListNode(value))
#         return True
#
#     def insertLast(self, value: int) -> bool:
#         if self.len == self.k:
#             return False
#         self.len += 1
#         self._add(self.tail.left, ListNode(value))
#         return True
#
#     def deleteFront(self) -> bool:
#         if self.len == 0:
#             return False
#         self.len -= 1
#         self._del(self.head)
#         return True
#
#     def deleteLast(self) -> bool:
#         if self.len == 0:
#             return False
#         self.len -= 1
#         self._del(self.tail.left.left)
#         return True
#
#     def getFront(self) -> int:
#         return self.head.right.val if self.len else -1
#
#     def getRear(self) -> int:
#         return self.tail.left.val if self.len else -1
#
#     def isEmpty(self) -> bool:
#         return self.len == 0
#
#     def isFull(self) -> bool:
#         return self.len == self.k

if __name__ == "__main__":
    obj = MyCircularDeque(5)
    obj.insertFront(3)
    print(obj.insertLast(4))
    print(obj.deque)
    print(obj.insertFront(2))
    print(obj.deque)
