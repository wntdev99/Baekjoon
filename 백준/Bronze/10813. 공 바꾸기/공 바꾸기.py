import sys

inputString = sys.stdin.readlines()
basketArray = list(range(1, int(inputString[0].split()[0]) + 1))
for inputNumbers in inputString[1:]:
    firstNum, secondNum = map(int, inputNumbers.split())
    tmpNum = basketArray[firstNum - 1]
    basketArray[firstNum - 1] = basketArray[secondNum - 1]
    basketArray[secondNum - 1] = tmpNum
print(' '.join(map(str, basketArray)))