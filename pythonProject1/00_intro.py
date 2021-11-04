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

# string을 사차식연산(식)으로 처리 
eval("1+2")


"""정규식"""
# 정규식 정규표현식 regex
# 문법 정리

# Groups and ranges
# Chracter	뜻
# |	또는      (Hi | Hello)
# ()	그룹  (Hi | Hello) | (and)  그룹 a 그룹b / gr(e|a)y
# []	문자셋, 괄호안의 어떤 문자든 gr[abcdef]y  gr[a-f]y [a-zA-Z0-9]
# [^]	부정 문자셋, 괄호안의 어떤 문가 아닐때 [^a-zA-Z0-9] 모든 대소문자, 숫자 제외
# (?:)	찾지만 기억하지는 않음  gr(?:e|a)y  그룹지정하지 않음

# Quantifiers
# Chracter	뜻
# ?	없거나 있거나 (zero or one)          gra?y > gry, gray  매치
# *	없거나 있거나 많거나 (zero or more)  gra*y > gry, gray, graaaay
# +	하나 또는 많이 (one or more)         gra+y >      gray, graaaaaaay
# {n}	n번 반복               gra{2}y  > graay
# {min,}	최소               gra{2,}y  > graay graaay graaaay
# {min,max}	최소, 그리고 최대  gra{2,3}y  > graay graaay

# Boundary-type
# Chracter	뜻
# \b	단어 경계          \bYa > Ya-- 앞에 Ya선택  //Ya\b > --Ya 뒤에 Ya선택
# \B	단어 경계가 아님   Ya\B > YaYa--  Ya중에서도 뒤에서 Ya가 안쓰이는
# ^	문장의 시작      ^Ya
# $	문장의 끝        Ya$

# Character classes
# Chracter	뜻
# \	특수 문자가 아닌 문자        \[\] 이렇게 찾아야함
# .	어떤 글자 (줄바꿈 문자 제외)
# \d	digit 숫자
# \D	digit 숫자 아님
# \w	word 문자
# \W	word 문자 아님
# \s	space 공백
# \S	space 공백 아님

import re
p = re.compile('ab*')
# match
p = re.compile('[a-z]+')
m = p.match('python') # 같냐 안같냐

# search
m = p.search('')

#findall 일치하는것을 찾아서 리스트로 리턴
#finditer 일치하는 것을 찾아서 이터레이터로 리턴

# 매치객체를 받아
m.group()
m.start()
m.end()
m.span()
