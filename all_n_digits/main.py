def all_n_digits(n):
  n_digits = []
  start = 10 ** (n - 1)
  end = (10 ** n) - 1
  for x in range(start, end):
    num = str(x)
    sum_of = sum([int(i) ** n for i in num])
    if sum_of == x:
      n_digits.append(x)
  return n_digits


def main():
  
  print(all_n_digits(4))



if __name__ == "__main__":
  main()

