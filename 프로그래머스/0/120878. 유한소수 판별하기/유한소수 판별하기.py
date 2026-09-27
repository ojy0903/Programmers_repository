import math

def solution(a, b):
    answer = 0

    gcd_val = math.gcd(a, b)
    div_b = b // gcd_val

    while div_b % 2 == 0:
        div_b //= 2

    while div_b % 5 == 0:
            div_b //= 5

    if div_b == 1:
        answer = 1
    else:
         answer = 2

    return answer