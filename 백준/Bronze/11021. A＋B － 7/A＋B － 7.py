import sys
caseCount = 1
for readLine in sys.stdin.readlines()[1:]:
    print(f"Case #{caseCount}: {sum(list(map(int, readLine.split())))}")
    caseCount += 1