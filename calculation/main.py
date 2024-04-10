def calculation(number):
  odds = 0
  evens = 0
  number = list(str(number))
  for x in range(len(number)):
    if x % 2 == 0:
      evens += int(number[x])
    else:
      odds += int(number[x])
  return evens - odds

def main():
  
    print(calculation(234567))


if __name__ == "__main__":
  main()

