def solve(s: str):
    new_str = s.split(' ')
    new_list = []
    for i in range(len(new_str)):
        new_list.append(new_str[i].capitalize())
    return ' '.join(new_list)
    
if __name__ == '__main__':

    s = input()

    result = solve(s)

    print(result)
