def split_and_join(line: str):
    string_split= line.split(" ")
    string_split = "-".join(string_split)
    return string_split

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
