import sys

num_cards = int(sys.stdin.readline().strip())
hand = list(sys.stdin.readline().strip().split(" "))
hand = [int(x) for x in hand]
hand.sort()

if num_cards == 1:
    result = int(hand[0])

elif num_cards == 2:
    if int(hand[0]) == int(hand[-1]) - 1:
        result = int(hand[0])
    else:
        result = int(hand[0]) + int(hand[1])

else:
    make_sum = [(hand[0])]

    for i in range(1, num_cards - 1):
        if (int(hand[i]) != int(hand[i - 1]) + 1):
            make_sum.append(hand[i])


    if (hand[-1] != int(hand[-2]) + 1):
        make_sum.append(hand[-1])


    result = 0
    for i in range(len(make_sum)):
        result += int(make_sum[i])

print(result)
