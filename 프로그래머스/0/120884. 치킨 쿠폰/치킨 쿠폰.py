def solution(chicken):
    service_chicken = 0
    coupon_count = chicken

    while (coupon_count // 10 > 0):
        chicken_given = coupon_count // 10
        service_chicken += chicken_given

        coupon_count = coupon_count % 10
        coupon_count += chicken_given

    answer = service_chicken
    return answer