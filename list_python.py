txt = "welcome to the jungle"
x = txt.split()
print(x)

# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. 
# Store them in a list and find the score of the runner-up.
n = int(input())
arr = map(int, input().split())
if 2<n<10:
    list_score = list(set(arr))
    list_score.sort()
    get_runner = list_score[-2]
else:
    print('n value exceeded')
