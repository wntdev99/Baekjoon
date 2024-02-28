import sys
studentNumbers = list(set(range(1,31)) - set(map(int, sys.stdin.readlines())))
print(f"{min(studentNumbers)}\n{max(studentNumbers)}")