#위장

def solution(clothes):
    a = {}
    for i in range(len(clothes)):
        if clothes[i][1] in a:
            a[clothes[i][1]] += 1
        else:
            a[clothes[i][1]] = 1
            
    count = 1
    for i in a.values():
        count *= i+1

    return count-1
######################################
def solution(clothes):
    closet = {}

    for i, j in clothes:
        if j not in closet:
            closet[j] = 1
        else:
            closet[j] += 1
    cnt = 1
    for i in closet.values():
        cnt *= i+1
    return cnt-1