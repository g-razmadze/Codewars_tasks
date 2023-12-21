def repeats(arr):
    counts = {}
    for num in arr:
        counts[num] = counts.get(num, 0) + 1
    return sum(key for key, value in counts.items() if value == 1)


def main():

    result = repeats([4,5,7,5,4,8])
    print(result)



if __name__ == "__main__":
    main()