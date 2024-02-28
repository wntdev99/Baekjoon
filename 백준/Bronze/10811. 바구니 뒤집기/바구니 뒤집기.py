import sys
inputNumbers = sys.stdin.readlines()
basketArray = list(range(1, int(inputNumbers[0].split()[0]) + 1))
for inputNumber in inputNumbers[1:]:
    firstNum, secondNum = map(int, inputNumber.split())
    basketArray[firstNum - 1: secondNum] = basketArray[firstNum - 1: secondNum][::-1]
print(' '.join(map(str,basketArray)))