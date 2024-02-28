import sys
caseCount = 1
for readLine in sys.stdin.readlines()[1:]:
    firstNum, secondNum = map(int, readLine.split())
    print(f"Case #{caseCount}: {firstNum} + {secondNum} = {firstNum + secondNum}")
    caseCount += 1