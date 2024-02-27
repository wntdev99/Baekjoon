inputHour, inputMinute = map(int,input().split())
setTime = inputHour * 60 + inputMinute - 45
if setTime < 0: setTime += 60 * 24
print(f"{setTime // 60} {setTime % 60}")