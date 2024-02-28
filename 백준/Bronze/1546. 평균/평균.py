import sys
inputString = sys.stdin.readlines()
inputNumbers = list(map(int, inputString[1].split()))
print(sum(list(map(lambda x: x / max(inputNumbers) * 100 / int(inputString[0]), inputNumbers))))