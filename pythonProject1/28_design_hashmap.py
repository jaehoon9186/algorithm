"""
28. 해시맵 디자인
706. Design HashMap
https://leetcode.com/problems/design-hashmap/

Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:
* MyHashMap() initializes the object with an empty map.
* void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
* int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
* void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.


Example 1:

Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]


Constraints:
* 0 <= key, value <= 10^6
* At most 10^4 calls will be made to put, get, and remove.

"""
# 내 풀이
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.dict[key] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key in self.dict.keys():
            return self.dict[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key in self.dict.keys():
            self.dict.pop(key)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# 풀이 1
# import collections
#
#
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, key=None, value=None):
#         self.key = key
#         self.value = value
#         self.next = None
#
#
# class MyHashMap:
#     # 초기화
#     def __init__(self):
#         self.size = 1000
#         self.table = collections.defaultdict(ListNode)
#
#     # 삽입
#     def put(self, key: int, value: int) -> None:
#         index = key % self.size
#         # 인덱스에 노드가 없다면 삽입 후 종료
#         if self.table[index].value is None:
#             self.table[index] = ListNode(key, value)
#             return
#
#         # 인덱스에 노드가 존재하는 경우 연결 리스트 처리
#         p = self.table[index]
#         while p:
#             if p.key == key:
#                 p.value = value
#                 return
#             if p.next is None:
#                 break
#             p = p.next
#         p.next = ListNode(key, value)
#
#     # 조회
#     def get(self, key: int) -> int:
#         index = key % self.size
#         if self.table[index].value is None:
#             return -1
#
#         # 노드가 존재할때 일치하는 키 탐색
#         p = self.table[index]
#         while p:
#             if p.key == key:
#                 return p.value
#             p = p.next
#         return -1
#
#     # 삭제
#     def remove(self, key: int) -> None:
#         index = key % self.size
#         if self.table[index].value is None:
#             return
#
#         # 인덱스의 첫 번째 노드일때 삭제 처리
#         p = self.table[index]
#         if p.key == key:
#             self.table[index] = ListNode() if p.next is None else p.next
#             return
#
#         # 연결 리스트 노드 삭제
#         prev = p
#         while p:
#             if p.key == key:
#                 prev.next = p.next
#                 return
#             prev, p = p, p.next

if __name__ == "__main__":
    obj = MyHashMap()
