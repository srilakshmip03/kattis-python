import sys
alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ_.")

rerun = True
while rerun:
    line = sys.stdin.readline().strip().split()
    rot = int(line[0])

    if rot == 0:
        break

    original = list(line[1])
    list.reverse(original)

    for i in range(len(original)):
        new_ind = ((alphabet.index(original[i])) + rot) % 28
        print(alphabet[new_ind], end = "")

    print()

