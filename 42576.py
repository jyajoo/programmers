from collections import Counter 

def new_func():
    p=	["marina", "josipa", "nikola", "vinko", "filipa"]
    c= ["josipa", "filipa", "marina", "nikola"]
    p = Counter(p)
    c = Counter(c)
    answer = ""
    for person, cnt in p.items():
        if p[person] != c[person]:
            answer += person
    return answer
print(new_func())