#전화번호 목록
#! 해시를 어떻게 이용해 주어야 하는가, 접두사 처리 어떻게 해주어야 하는지..

#? 해시 이용X
def solution(pb):
    pb.sort()
    cnt = 0
    for i in range(len(pb)):
        for j in pb[i+1:]:    #i 다음번째부터 확인
            if pb[i] == j[:len(pb[i])]: # 처음부터 i 길이만큼 비교해주며 접두어인지 확인
                return False
    return True
# ##############################################
#얘를 간략하게 한 게 윗코드
def solution(pb):
    for i in range(len(pb)-1):
        for j in range(i+1,len(pb)):
            if len(pb[i]) <= len(pb[j]):
                if pb[i] == pb[j][:len(pb[i])]:
                    return False
            else:
                if pb[j] == pb[i][:len(pb[j])]:
                    return False
    return True
#######################################################
#? startswith():접두사인지 아닌지 판별하는 함수

def solution(pb):
    for i in pb:
        for j in pb:
            if i != j and j.startswith(i):
                return False
    return True
#
def solution(pb):
    pb.sort()
    for i, j in zip(pb, pb[1:]):
        if j.startswith(i):
            return False
    return True
#* j가 i 다음번째부터 비교해야하는 경우) i!=j라는 조건을 추가하거나, zip으로 묶기
############################################################
#hash 이용하는 코드라고 합니다..!
def solution(pb):
    hash = {}
    for i in pb:
        hash[i] = 1
    for i in pb:
        temp = ""
        for j in i:
            temp += j
            if temp in hash and temp != i:
                return False
    return True