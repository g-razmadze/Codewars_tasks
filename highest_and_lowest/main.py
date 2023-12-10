def high_and_low(numbers):
    num = sorted([int(x) for x in numbers.split()])
    return f"{num[-1]} {num[0]}"