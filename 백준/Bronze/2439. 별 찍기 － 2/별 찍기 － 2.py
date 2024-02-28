import sys
inputNumber = int(sys.stdin.readline())
for i in range(1, inputNumber + 1):
    print(f"{' ' * (inputNumber - i)}{'*' * i}")