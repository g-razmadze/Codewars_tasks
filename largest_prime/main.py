def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True



def largest_prime_in_integer(num):
    num_str = str(num)
    largest_prime = None

    for i in range(len(num_str)):
        for j in range(i + 1, len(num_str) + 1):
            substring = num_str[i:j]
            substring_int = int(substring)
            if is_prime(substring_int):
                if largest_prime is None or substring_int > largest_prime:
                    largest_prime = substring_int

    return largest_prime



def main():
  
    result = largest_prime_in_integer(1234)
    print(result)


if __name__ == "__main__":
  main()

