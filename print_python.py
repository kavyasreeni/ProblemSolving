# The included code stub will read an integer,n, from STDIN.

# Without using any string methods, try to print the following: 123..n

# Note that "" represents the consecutive values in between.

n = int(input('Enter number: '))

# Method 1
result = 1
while result<=n:
    print(result, end='')
    result += 1

# Method 2
for number in range(1,n+1):
    print(number, end='')
