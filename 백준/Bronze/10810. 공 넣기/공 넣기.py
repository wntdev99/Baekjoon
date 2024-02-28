N, M = map(int, input().split())
basketArray = [0] * N

for _ in range(M):
    firstNum, secondNum, thirdNum = map(int, input().split())
    for basketNum in range(firstNum - 1, secondNum):
        basketArray[basketNum] = thirdNum
print(' '.join(map(str, basketArray)))