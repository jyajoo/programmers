#완주하지 못한 선수

from collections import Counter 

def solution(p, c):
    p = Counter(p)
    c = Counter(c)
    answer = ''
    for person, cnt in p.items():
        if p[person] != c[person]:
            answer += person
    return answer

#####################################
#완주하지 못한 선수_2
from collections import Counter 

def solution(p, c):
    p = dict(Counter(p))
    c = dict(Counter(c))
    answer = ''
    for person, cnt in p.items():
        try:
            if p[person] != c[person]:
                answer += person
        except:
            answer += person
    return answer
####*다른 사람 풀이도 참고하기!