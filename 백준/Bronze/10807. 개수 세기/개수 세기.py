import sys
inputString = sys.stdin.readlines()
print(list(map(int,inputString[1].split())).count(int(inputString[2])))