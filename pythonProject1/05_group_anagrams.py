"""
05 그룹 애너그램
49.Group Anagrams
https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
* 1 <= strs.length <= 104
* 0 <= strs[i].length <= 100
* strs[i] consists of lower-case English letters.


"""

# 내 풀이 (답 참고)
import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 유사 딕셔너리?
        answer = collections.defaultdict(list)

        for a in strs :
            # 정렬하여 딕셔너리에 추가
            answer[''.join(sorted(a))].append(a)
            # eat, ate  ->  ''.join(sorted(a)) -> aet : 동일한 키 값을 가짐

        print(answer)
        return answer.values()

if __name__=="__main__":
    sol = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    sol.groupAnagrams(strs)


# 풀이 1
#
# import collections
# from typing import List
#
#
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         anagrams = collections.defaultdict(list)
#
#         for word in strs:
#             # 정렬하여 딕셔너리에 추가
#             anagrams[''.join(sorted(word))].append(word)
#         return list(anagrams.values())
