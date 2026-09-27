def solution(quiz):
    result_list = []
    
    for equation in quiz:
        # 각 수식을 공백 기준 split & 숫자와 연산자 추출
        term_list = equation.split(" ")
        num1 = int(term_list[0])
        num2 = int(term_list[2])
        num3 = int(term_list[4])
        operation = term_list[1]
        
        # 연산자에 따라 실제 연산 진행 & OX 여부 판정
        match operation:
            case "+":
                is_correct = (num1 + num2 == num3)
                result_list.append('O' if is_correct else 'X')
            case "-":
                is_correct = (num1 - num2 == num3)
                result_list.append('O' if is_correct else 'X')

    answer = result_list
    return answer