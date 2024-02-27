inputHour, inputMinute = map(int,input().split())
inputTime = int(input())

currentTime = inputHour * 60 + inputMinute
finishTime = currentTime + inputTime

outputHour = finishTime // 60 % 24
outputMinute = finishTime % 60

print(f"{outputHour} {outputMinute}")