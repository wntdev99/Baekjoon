import sys
inputString = sys.stdin.readlines()
standardNum = int(inputString[0].split()[1])
print(*[tmpNum for tmpNum in list(map(int, inputString[1].split())) if tmpNum < standardNum])