def count_divisible_numbers_less_than(n: int):
    count = 0
    for k in range(2, n+1):
        not_prime = False
        for i in range(2, k):
            if k%i == 0:
                not_prime = True
        if not_prime:
            count+=1
    print(count)