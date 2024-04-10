def binary_representation(st):
  ints = []
  for i in st:
    ints.append(ord(i))
  return [bin(i)[2:] for i in ints]

def main():
  
  print(binary_representation("Hello"))



if __name__ == "__main__":
  main()

