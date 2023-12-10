def is_isogram(string):
    return list(sorted(set(string.lower()))) == sorted(list(string.lower()))