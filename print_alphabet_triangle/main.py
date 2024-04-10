def print_alphabet_triangle3(n):
    for i in range(n):
      print(" " * (n - i - 1) + " ".join(chr(65 + j) for j in range(i + 1)))




def main():
   
    print(print_alphabet_triangle3(5))


if __name__ == "__main__":
   main()

