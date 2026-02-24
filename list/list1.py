import sys

list = [10, 24, 49, 49, 94, 101, 23, 78, 90, 67]
max = list[0]
for i in range(len(list)):
    if (list[i] > max):
        max = list[i]

print(max)