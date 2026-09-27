def solution(polynomial):
    poly_list = polynomial.split(" + ")

    x_sum, num_sum = 0, 0
    for character in poly_list:
        if character.endswith("x"):
            coef = character[:-1]
            # 추출한 x 의 계수가 존재하지 않으면 1로 처리, 있으면 해당 계수로 처리
            x_sum += int(coef) if coef else 1 
        else:
            num_sum += int(character)

    terms = []
    if x_sum:
        # x 계수가 1이면 'x', 아니면 계수 붙이기
        terms.append('x' if x_sum == 1 else f'{x_sum}x')
    if num_sum:
        # 상수항이 있다면 더하기, 없으면 표기 안함
        terms.append(str(num_sum))

    answer = " + ".join(terms)
    return answer
