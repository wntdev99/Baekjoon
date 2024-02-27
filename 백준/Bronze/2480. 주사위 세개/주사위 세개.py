from collections import Counter

inputNumbers = list(map(int, input().split()))

if len(set(inputNumbers)) == 1: print(10000 + inputNumbers[0] * 1000)
elif len(set(inputNumbers)) == 3: print(max(inputNumbers) * 100)
else: print(1000 + [item for item, count in Counter(inputNumbers).items() if count == 2][0] * 100)