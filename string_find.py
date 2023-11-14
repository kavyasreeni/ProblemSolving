# ABCDCDC CDC o/p = 2
# Method_1
def count_substring(string:str, sub_string:str):
    len_sub_string = len(sub_string)
    result = 0
    for i in range(len(string)):
        if string[i:i+len_sub_string] == sub_string:
            result += 1   
    return result

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

# Method_2
def count_substring(valstr:str, sub_string:str):
    count = 0
    for i in range(len(valstr)):
        if valstr[i:].startswith(sub_string):
            count += 1   
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)