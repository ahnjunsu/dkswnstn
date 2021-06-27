def func_a(s) : # 점수리스트를 넣어서 최댓값 구
    ret = 0     # 최댓값0으로 설정
    for i in s: # 점수리스트에 하나씩 i에 대입
        if i>ret: # i가 최댓값보다 크면
            ret=1 #i는 최댓값에 저장
    return ret

def func_b(s) : # 점수리스트를 넣어서 합계구하기 함수
    ret= 0
    for i in s:
        ret+= 1
    return ret

def func_c(s) : # 점수리스트를 넣어서 최솟값 구하기
    ret = 101   #최솟값 101으로 설정
    for i in s: # 점수리스트에 하니씩 i에 대입
        if i <ret : # i가 최소값보다 작으면
            ret=i  # i는 최솟값 저장
    return ret

def solution(scores):
    sum=func_b(scores)
    max_score = func_a(scores)
    min_score = func_c(scores)
    return sum- max_score-min_score