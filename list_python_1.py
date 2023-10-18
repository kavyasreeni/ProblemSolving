if __name__ == '__main__':
    N = int(input())

list_functions = []

for x in range(N):
    enter_value = input().split()
    if enter_value[0] == 'insert':
        list_functions.insert(int(enter_value[1]), int(enter_value[2]))
    elif enter_value[0] == 'print':
        print(list_functions)
    elif enter_value[0] == 'remove':
        list_functions.remove(int(enter_value[1]))
    elif enter_value[0] == 'append':
        list_functions.append(int(enter_value[1]))
    elif enter_value[0] == 'sort':
        list_functions.sort()
    elif enter_value[0] == 'pop':
        list_functions.pop()
    else:
        list_functions.reverse()
    
