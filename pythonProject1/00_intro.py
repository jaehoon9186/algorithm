"""
출처 파이썬 알고리즘 인터뷰  박상길 저
책을 읽으며

문제출처 : 리트코드
leetcode.com

깃허브 answer
https://github.com/onlybooks/algorithm-interview



유튜브 문풀 (by Chris AI Holic 님)
https://www.youtube.com/watch?v=yp1leTBR5ko&list=PL1iR1v6eNy5OO01XbQ1djo4P6gNG78wYH



코드스니펫만들것
깃허브 기스트 활용?
인터넷 모음집 참고해볼것


파이썬은 다른언어에 비해 느리기 때문에 알고리즘 최적화에 신경쓸 것

예외 처리를 잊지 말것

repl도구로 코드검증할것

화이트보드 코딩 인터뷰
문제해결 - 코딩 - 검증 - 커뮤니케이션

"""

""" 배열 """
# 요소 파악
# 딕셔너리 자료형으로 key랑 갯수 리턴
# 문자열을 하나씩 뽑고 딕셔너리로 선언된 변수에 넣어도 될듯 +=1
d1 = collections.Counter(배열)

# 비교 생략
freqs = collections.defaultdict(int)