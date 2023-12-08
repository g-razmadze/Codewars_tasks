def remove_smallest(numbers):
    if not numbers:
        return []
    nnum = numbers[:]
    min_num = nnum.index(min(nnum))
    pop = nnum.pop(min_num)
    return nnum