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

# s 문자열의 인덱스번호, 문자 리턴 반복
for index, char in enumerate(s):

# 딕셔너리 -> 튜플 -> value 값으로 정렬 x[0] 키로 , x[1]값으로
# 값으로 키 정렬  -> 딕셔너리로 ->  키값만 리스트로 리턴
list(dict(sorted(answer.items(), key=lambda x: x[1], reverse=True)).keys())


#진수 변환
bin(숫자), oct(), hex()
0b1010, 0o블라블라, 0x블라블라
format(42, 'b') -> 42 2진수로 변환
format(42, '#o') -> +접두어

int('0b101010', 2), int('0o52', 8), int('0x2a', 16)

# 문자열 바꾸기
str1.replace('old', 'new')

# 문자열 갯수 맞추기
str.zfill(8)
str.ljust(8, '0')
str.rjust(8, '0')

# 절대값
abs(5-2)