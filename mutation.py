# Method_1
def mutate_string(string: str, position:int, character:str):
    
    return string[:position]+character+string[position:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

# sample input
"""
STDIN           Function
-----           --------
abracadabra     s = 'abracadabra'
5 k             position = 5, character = 'k'
"""
# sample output
# abrackdabra

# Method_2
def mutate_string(string: str, position:int, character:str):
    list_convert = list(string)
    list_convert[position] = character
    string = ''.join(list_convert)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
