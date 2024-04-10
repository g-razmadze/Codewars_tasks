def list_item_to_tuple_of_two(lst):
    result = []
    for i in range(0, len(lst), 2):
        if i + 1 < len(lst):
            result.append((lst[i], lst[i + 1]))
        else:
            result.append((lst[i],))
    return result


def main():
  
    input_list1 = [1, 2, 3, 4, 5, 6, 11, 45, 'd', 'e', 'f', 'g', 'h', 'i']
    output1 = list_item_to_tuple_of_two(input_list1)
    print(output1)

    input_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    output2 = list_item_to_tuple_of_two(input_list2)
    print(output2)




if __name__ == "__main__":
  main()

