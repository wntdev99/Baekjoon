import sys
inputNumbers = list(map(int, sys.stdin.readlines()[1].split()))
print(f"{min(inputNumbers)} {max(inputNumbers)}")