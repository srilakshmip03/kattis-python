
import math
import sys

info = sys.stdin.readline()
info_list = info.split()
# info_list[0] is the height of the wall, [1] is the angle from the ground

hyp = int(info_list[0]) / (math.sin(math.radians(int(info_list[1]))))

print(math.ceil(hyp))
