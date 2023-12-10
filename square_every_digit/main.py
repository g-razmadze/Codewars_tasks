def square_digits(num):
    result = ""
    for x in str(num):
        square =  int(x)**2
        result += str(square)
    return int(result)