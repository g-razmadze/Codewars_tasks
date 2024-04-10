def read_names_file(file_path):

    name_lengths = {}

    try:
        with open(file_path, 'r') as f:
            for line in f:
                name = line.strip()
                length = len(name)
                if length in name_lengths:
                    name_lengths[length] += 1
                else:
                    name_lengths[length] = 1
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None

    return name_lengths


def main():

    file_path = "names.txt"
    result = read_names_file(file_path)
    for length, count in result.items():
        print(f"Length {length}: {count} names")


if __name__ == "__main__":
    main()

