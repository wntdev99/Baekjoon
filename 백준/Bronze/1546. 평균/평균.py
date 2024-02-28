import sys
inputString = sys.stdin.readlines()
inputNumbers = list(map(int, inputString[1].split()))
setNumbers = list(map(lambda x: x / max(inputNumbers) * 100, inputNumbers))
print(sum(setNumbers) / int(inputString[0]))