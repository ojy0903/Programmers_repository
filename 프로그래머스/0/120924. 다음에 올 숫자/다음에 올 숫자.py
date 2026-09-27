def solution(common):
    diff_first = common[1] - common[0]
    diff_second = common[2] - common[1]

    if diff_first == diff_second:
        answer = common[-1] + diff_first
    else:
        diff_mul = diff_second // diff_first
        answer = common[-1] * diff_mul
    
    return answer