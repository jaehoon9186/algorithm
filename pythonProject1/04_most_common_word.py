"""
04 가장 흔한 단어
819. most common word
https://leetcode.com/problems/most-common-word/

Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned.
It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.

Example 1:
Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation:
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"),
and that "hit" isn't the answer even though it occurs more because it is banned.

Example 2:
Input: paragraph = "a.", banned = []
Output: "a"

Constraints:
* 1 <= paragraph.length <= 1000
* paragraph consists of English letters, space ' ', or one of the symbols: "!?',;.".
* 0 <= banned.length <= 100
* 1 <= banned[i].length <= 10
* banned[i] consists of only lowercase English letters.

"""

# 내 풀이
import re
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        answer = ''

        # 문자열 문자를 제외한 나머지 공백으로 바꾸기
        # 여기서 소문자로 바꿔줘도
        str1 = re.sub(r'[\W]', ' ', paragraph.lower())

        # 문자열 공백으로 나누기 .split()으로 리스트로 변환
        paragraph_list = str1.split(' ')

        # 람다 표현식으로 리스트에서 공백 제거
        paragraph_list = list(filter(lambda a: a != '', paragraph_list))

        # banned list에 지정된 문자열은 제외
        paragraph_list = [a for a in paragraph_list if a not in banned]

        # 가장 빈도수가 높은 value를 찾아라
        max = 0
        for a in paragraph_list:
            if paragraph_list.count(a) > max:
                max = paragraph_list.count(a)
                answer = a

        print(answer)

        return answer


sol = Solution()
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
sol.mostCommonWord(paragraph, banned)


# 풀이 1

# import collections
# import re
# from typing import List
#
#
# class Solution:
#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#         words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
#         print(words)
#         # > ['bob', 'a', 'ball', 'the', 'ball', 'flew', 'far', 'after', 'it', 'was']
#
#         counts = collections.Counter(words)
#         print(counts)
#         # > Counter({'ball': 2, 'bob': 1, 'a': 1, 'the': 1, 'flew': 1, 'far': 1, 'after': 1, 'it': 1, 'was': 1})
#
#         print(counts.most_common(1))
#         # > [('ball', 2)]
#
#         # 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴
#         return counts.most_common(1)[0][0]
#
#
# sol = Solution()
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
# sol.mostCommonWord(paragraph, banned)
#
