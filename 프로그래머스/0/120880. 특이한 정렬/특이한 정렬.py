def solution(numlist, n):
    answer = []

    # numlist 를 정렬한다
    # 1. 기본 정렬 기준은 abs(x-n) 값 : numlist 내부 요소 값과 n 사이 거리값
    # 2. 만약 거리값이 같으면 -x 값 : x 값이 클수록 -x 값은 더 작아져 더 큰 우선순위를 가진다
    sorted_list = sorted(numlist, key=lambda x: (abs(x - n), -x))
    answer = sorted_list

    return answer