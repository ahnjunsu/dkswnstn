def solution(scores):
    grade_counter = [0 for  i in range(5)]
        # grade_computer : 학점목록에 학점[A-f]  5개을 0으로 설정

    for x in scores : # 점수목록에서 하나씩 x에 대입
        if x >= 85 : # x 가 85점 이상이면
            grade_counter[0] +=1        # 학점목록[1] = b 학점 한명추가????
        elif x >= 70 : # x 가 85점 이상이면
            grade_counter[1] +=1        # 학점목록[1] = b 학점 한명추가????
        elif x >= 55 : # x 가 85점 이상이면
            grade_counter[2] +=1        # 학점목록[1] = b 학점 한명추가
        elif x >= 44 : # x 가 85점 이상이면
            grade_counter[3] +=1        # 학점목록[1] = b 학점 한명추가
        else : # x 가 85점 이상이면
            grade_counter[4] +=1        # 학점목록[1] = b 학점 한명추가

    return grade_counter