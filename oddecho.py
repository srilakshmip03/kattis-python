import sys

num_lines = sys.stdin.readline()
num_lines = int(num_lines)

result = []

for i in range(num_lines):
    word = sys.stdin.readline()
    result.append(word)
    
for i in range(num_lines):
    ind = i
    if i % 2 == 0:
        print(result[i])