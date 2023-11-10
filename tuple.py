# using hash built_in_function

if __name__ == '__main__':
    n = int(input())
    finalList = map(int, input().split())
    t = tuple(finalList)
    print(hash(t))
