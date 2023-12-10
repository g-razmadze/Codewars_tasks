def divisors(n):
    divisors_list = []
    for i in range(2, n):
        if n % i == 0:
            divisors_list.append(i)
    if len(divisors_list) == 0:
        return str(n) + " is prime"
    else:
        return divisors_list