import sys

array = sys.stdin.readline().split()

result = 1
for i in array:
    result *= int(i)
print(result)
