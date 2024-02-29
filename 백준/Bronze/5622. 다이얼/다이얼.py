import sys
outputTime = 0
inputString = sys.stdin.readline().strip()

for tmpString in inputString:
    if ord(tmpString) >= 80:
        if ord(tmpString) < 84:
            outputTime += 8
        elif ord(tmpString) < 87:
            outputTime += 9
        else:
            outputTime += 10
    else:
        outputTime += (ord(tmpString) - 65) // 3 + 3

print(outputTime)