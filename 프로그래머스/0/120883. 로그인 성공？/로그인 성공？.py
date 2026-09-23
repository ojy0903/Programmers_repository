def solution(id_pw, db):
    answer = 'fail'
    
    id = id_pw[0]
    pw = id_pw[1]
    
    for info in db:
        if info[0] == id:
            if info[1] == pw:
                answer = 'login'
                break
            else:
                answer = 'wrong pw'
                break 
    
    return answer