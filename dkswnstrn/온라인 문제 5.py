def solution(arr, k):
    # arr : 2차원 리스트
    # k : k번째 작은수
    answer = 0 # k번째 작은수 변수

    list = [] # 임시 리스트
    n = len(arr) # n은 배열의 세로길이

    #2차원 리스트 => 1차원리스트 변경
    for i in range(n): # n 은 배열의 세로 길이
        for j in range(4): # 4는 배열의 가로길이
            list.append(arr[i][j])
            # 2차원리스트 값을 1차원 리스트 저장

    # 정렬 => sort : 오름차순으로 정렬하기
    list.sort()
    # k번째 => 인덱스 [k-1] : 이유 : 인덱스는 0번부터 시작
    answer = list[k - 1]
    return answer
