def sublist(lst):
    all_sublists = []
    n = len(lst)

    for i in range(n):
        for j in range(i + 1, n + 1):
            all_sublists.append(lst[i:j])

    return all_sublists


def main():
   
    input_list = [1, 2, 3]
    output = sublist(input_list)
    print(output)


if __name__ == "__main__":
   main()
