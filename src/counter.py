def count_ocurrences(path, word):
    file = open(path, "r")
    read_data = file.read()
    word_count = read_data.lower().count(word.lower())
    print(word_count)
    return word_count
