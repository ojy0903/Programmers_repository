def solution(array):
    # array 내부 서로 다른 수를 Set 으로 추출
    num_set = set(array)
    # dictionary 사용, 각각의 수: key, array 내부 갯수: value 
    num_dict = {}
    for num in num_set:
        num_dict[num] = 0

    # 각 key 값에 대한 array 내부 갯수 세기
    for num in array:
        num_dict[num] += 1

    # 최빈값 (max_key) 찾기
    max_count, max_key = 0, 0
    for key in num_dict.keys():
        if num_dict.get(key) > max_count:
            max_count = num_dict.get(key)
            max_key = key

    answer = max_key
    # 만약 최빈값과 갯수가 같은 다른 값이 있으면 answer = -1
    for key in num_dict.keys():
        if key == max_key:
            continue
        elif num_dict.get(key) == max_count:
            answer = -1

    return answer