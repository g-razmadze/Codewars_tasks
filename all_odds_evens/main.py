def all_odds_evens(num):
  odds = []
  evens = []
  num = list(str(num))
  all_sublists = []
  n = len(num)

  for i in range(n):
    for j in range(i + 1, n + 1):
        all_sublists.append(num[i:j])
  for x in all_sublists:
    number = "".join(x)
    number = int(number)
    if number % 2 == 0:
      evens.append(number)
    else:
      odds.append(number)
  return odds, evens


def main():
  
    print(all_odds_evens(12345))


if __name__ == "__main__":
  main()

