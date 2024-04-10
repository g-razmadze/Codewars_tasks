def is_prime(n):
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True


def word(st):
  s = ""
  for i in range(len(st)):
    if is_prime(i):
      s += st[i]
  return s

def main():
  word("Mathematics is the music of reason.")
  print(word)


if __name__ == "__main__":
  main()

