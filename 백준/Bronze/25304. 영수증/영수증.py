import sys

totalPrized = 0
inputString = sys.stdin.read().splitlines()
for objectList in inputString[2:]:
    objectPrize, objectAmount = map(int, objectList.split())
    totalPrized  += objectPrize * objectAmount
print("Yes") if int(inputString[0]) == totalPrized else print("No")